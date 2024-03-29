import json
import os

import rich_click as click  # type: ignore

from rich.panel import Panel
from rich.markdown import Markdown

from typing import Optional, Iterable, Type

from rich.status import Status

from typing import Iterable

from squiz import __version__
from squiz.types import types
from squiz.logger import Logger, console
from squiz.abc import BaseType, BaseModule, BaseModel

from inspect import getmembers, isclass
from importlib import import_module


BaseModuleType = Type[BaseModule]


def load_modules(path: str = "modules") -> Iterable[BaseModuleType]:
    """Load all modules"""

    for i in os.listdir(path):
        if i.startswith("__"):
            continue

        elif i.endswith(".py"):
            yield from load_module(
                f'{".".join(path.split(os.path.sep))}' "." f'{i.removesuffix(".py")}'
            )

        else:
            if os.path.isdir(new_path := os.path.join(path, i)):
                yield from load_modules(new_path)


def load_module(module: str) -> Iterable[BaseModuleType]:
    """Load a module"""

    for _, module_class in getmembers(import_module(module)):
        if isinstance(module_class, BaseModule) or module_class == BaseModule:
            continue

        if isclass(module_class) and issubclass(module_class, BaseModule):
            yield module_class


def execute_many_modules(
    modules: Iterable[BaseModule], progress: bool = True, **kwargs
) -> list[BaseModel] | None:
    """Execute many modules"""
    results = []

    if progress:
        with Status("Running modules...", console=console) as status:
            for module in modules:
                if isinstance(status, Status):
                    status.update(f"Running modules... ({module.name})")

                result = module_executor(module, **kwargs)

                if result is None:
                    continue

                results.extend(result)
    else:
        for module in modules:
            result = module_executor(module, **kwargs)

            if result is None:
                continue

            results.extend(result)

    return results


def module_executor(cls: BaseModule, **kwargs) -> list[BaseModel] | None:
    """Execute a module"""

    try:
        cls.execute(**kwargs)
    except Exception as e:
        Logger.debug(f"Error running module: {cls.name}: {e}")

    if not (results := cls.results):
        return None

    for result in results:
        print()

        table = result.__rich__()
        table.title = cls.name

        console.print(table)

    return cls.results


def get_modules(target: BaseType) -> Iterable[BaseModule]:
    """Returns a list of modules that can be executed"""
    yield from map(
        lambda x: x(),
        filter(lambda x: target.__class__ in x.target_types, load_modules()),
    )


def parse_target(target: str) -> list[BaseType] | None:
    """Parses the target string"""

    if a := list(filter(lambda x: x.validate(target), types)):
        return list(map(lambda tpe: tpe(value=target), a))

    return None


@click.command()
@click.option("-h", "--help", is_flag=True, help="Show help message and exit")
@click.option("-n", "--hide-banner", is_flag=True, help="Hide the banner")
@click.option("-u", "--update", is_flag=True, help="Update Squiz")
@click.option("-V", "--version", is_flag=True, help="Show version and exit")
@click.argument("target", required=False)
def run(
    help: Optional[bool] = False,
    update: Optional[bool] = False,
    hide_banner: Optional[bool] = False,
    version: Optional[bool] = False,
    target: Optional[str] = None,
) -> None:
    if hide_banner is not True:
        Logger.print_banner()

    if help is True:
        return console.print(
            Panel(
                Markdown(
                    """
### *Usage*
> * `squiz [options] [target]`

### *Required arguments*
> * `target`: The target to scan.

### *Options*
> * `-h, --help` - Show help message and exit

> * `-u, --update` - Update Squiz (git)

> * `-n, --hide-banner` - Hide the banner

> * `-V, --version` - Show version and exit

                    """
                ),
                width=50,
                border_style="bright_black",
            )
        )

    if version:
        Logger.info(f"Squiz 'v{__version__}'")
        return

    if update is True:
        os.system("git fetch")
        os.system("git pull")

    if target is None:
        return Logger.fatal("No target specified")

    target_types = parse_target(target)

    if target_types is None:
        return Logger.fatal(f"Invalid target: {target}")

    Logger.info(f"Running modules...")

    for target_type in target_types:
        modules = get_modules(target_type)

        if not modules:
            return Logger.fatal(f"No modules found for target: {target}")

        results_lst = [
            model.dump()
            for model in execute_many_modules(modules, target=target_type) or []
        ]

        json.dump(results_lst, open(f"results_{target}.json", "w+"))

    Logger.success("Done!")
