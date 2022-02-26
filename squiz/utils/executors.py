import typing

from rich.status import Status

from squiz.base import BaseModule, BaseModel
from squiz.logger import Logger, console
from squiz.utils.decorators import debug


@debug
def execute_many_modules(
    modules: typing.Iterable[BaseModule], progress: bool = True, **kwargs
) -> typing.Optional[typing.List[BaseModel]]:
    """ Execute many modules """

    class __:
        def __enter__(self): ...
        def __exit__(self, *_): ...

    results = []

    with Status("Running modules...", console=console) if progress else __():
        for module in modules:
            result = module_executor(module, **kwargs)

            if result is None:
                continue

            results.extend(result)

    return results


def module_executor(
    cls: BaseModule, **kwargs
) -> typing.Optional[typing.List[BaseModel]]:
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
        console.print(row)

    return cls.results
