from rich.status import Status
from rich.columns import Columns

from typing import Iterable, List, Optional

from squiz.abc import BaseModule, BaseModel
from squiz.logger import console


def execute_many_modules(
    modules: Iterable[BaseModule], progress: bool = True, **kwargs
) -> Optional[List[BaseModel]]:
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


def module_executor(cls: BaseModule, **kwargs) -> Optional[List[BaseModel]]:
    """Execute a module"""

    try:
        cls.execute(**kwargs)
    except Exception:
        return None

    if not cls.results:
        return None

    s = f"Result(s) for module: {cls.name}"
    console.print(f"\n[bold white]{s}[/]\n{'-' * len(s)}")

    console.print(Columns(cls.results, expand=True), highlight=False)

    return cls.results
