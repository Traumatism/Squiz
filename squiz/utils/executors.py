from typing import Iterable, List, Optional

from rich.status import Status

from ..base import BaseModule, BaseModel
from ..logger import Logger, console


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


def module_executor(
    cls: BaseModule, **kwargs
) -> Optional[List[BaseModel]]:
    """ Execute a module """

    try:
        state = cls.execute(**kwargs)
    except Exception as e:
        return Logger.error(
            f"Error while executing module {cls.name}: {e}"
        )

    if isinstance(state, BaseModule.State):
        if isinstance(state, BaseModule.ExecutionSuccess):
            Logger.info(f"Successfully executed module {cls.name}")

        if isinstance(state, BaseModule.ExecutionError):
            Logger.error(
                f"Potential Error while executing module {cls.name}: "
                f"{state.message}"
            )

    if not cls.results:
        return

    s = f'Result(s) for module: {cls.name}'
    console.print(f"\n[bold white]{s}[/]\n{'-' * len(s)}")

    del s

    for row in cls.results:
        console.print(row, highlight=False)

    return cls.results
