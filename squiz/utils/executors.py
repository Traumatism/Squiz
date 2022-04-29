from rich.status import Status

from typing import Iterable, List, Optional

from squiz.base import BaseModule, BaseModel
from squiz.logger import console


def execute_many_modules(
    modules: Iterable[BaseModule], progress: bool = True, **kwargs
) -> Optional[List[BaseModel]]:
    """Execute many modules"""
    MSG = "Running modules... %(module)s"

    results = []

    if progress:
        with Status(MSG % {"module": ""}, console=console) as status:

            for module in modules:

                if isinstance(status, Status):
                    status.update(MSG % {"module": f"({module.name})"})

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

    s = f'Result(s) for module: {cls.name}'
    console.print(f"\n[bold white]{s}[/]\n{'-' * len(s)}")

    for row in cls.results:
        console.print(row, highlight=False)

    return cls.results
