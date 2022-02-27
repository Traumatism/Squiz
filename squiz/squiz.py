
import rich_click as click

from rich.panel import Panel
from rich.markdown import Markdown

from typing import Optional, Iterable

from .types import types
from .load import load_modules
from .base import BaseType, BaseModule
from .logger import Logger, console
from .utils.executors import execute_many_modules


def get_modules(target: BaseType) -> Iterable[BaseModule]:
    """ Returns a list of modules that can be executed """
    return map(lambda x: x(), filter(
        lambda x: target.__class__ in x.target_types, load_modules()
    ))


def parse_target(target: str) -> Optional[BaseType]:
    """ Parses the target string """
    ts = list(filter(lambda x: x.validate(target), types))

    if len(ts) == 1:
        return ts[0](target)

    if not ts:
        return Logger.fatal(f"Invalid target: {target}")

    return Logger.fatal(f"Ambiguous target: {target}")


@click.command()
@click.option(
    "-h", "--help",
    is_flag=True,
    help="Show help message and exit",
    default=True
)
@click.argument("target", required=False)
def run(help: Optional[bool] = False, target: Optional[str] = None) -> None:
    Logger.print_banner()

    if help is True:
        return console.print(Panel(Markdown(
            """
### *Usage*
> * `squiz [options] [target]`

### *Required arguments*
> * `target`: The target to scan.

### *Options*
> * `-h, --help` - Show help message and exit

> * `-v, --version` - Show version and exit

            """
        ), width=50, border_style="bright_black"))

    if target is None:
        return Logger.fatal("No target specified")

    target_type = parse_target(target)

    if target_type is None:
        return

    modules = get_modules(target_type)

    if not modules:
        return

    Logger.info("Running modules...")

    execute_many_modules(modules, **{"target": target_type})

    Logger.success("Done!")


run()
