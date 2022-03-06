from rich.status import Status

from typing import Iterable, List, Optional

from ..base import BaseModule, BaseModel
from ..logger import console


def execute_many_modules(
    modules: Iterable[BaseModule], progress: bool = True, **kwargs
) -> Optional[List[BaseModel]]:
    """ Execute many modules """
    MSG = "Running modules... %(module)s"

    class __:
        def __enter__(self): ...
        def __exit__(self, *_): ...

    results = []

    with Status(
        MSG % {"module": ""}, console=console
    ) if progress else __() as status:

        for module in modules:

            if isinstance(status, Status):
                status.update(MSG % {"module": "(%s)" % module.name})

            result = module_executor(module, **kwargs)

            if result is None:
                continue

            results.extend(result)

    return results


def module_executor(cls: BaseModule, **kwargs) -> Optional[List[BaseModel]]:
    """ Execute a module """

    try:
        cls.execute(**kwargs)
    except Exception:
        return

    if not cls.results:
        return

    s = f'Result(s) for module: {cls.name}'
    console.print(f"\n[bold white]{s}[/]\n{'-' * len(s)}")

    for row in cls.results:
        console.print(row, highlight=False)

    return cls.results
