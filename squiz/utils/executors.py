from rich.status import Status
from rich.panel import Panel

from typing import Iterable

from squiz.logger import Logger
from squiz.abc import BaseModule, BaseModel
from squiz.logger import console


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
