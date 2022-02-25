import typing

from squiz.logger import Logger, console
from squiz.base import BaseModule, BaseModel
from squiz.utils.decorators import add_debug


@add_debug
def execute_many(
    modules: typing.Iterable[BaseModule], **kwargs
) -> typing.Optional[typing.List[BaseModel]]:
    """ Execute many modules """

    results = []

    for module in modules:
        result = module_executor(module, **kwargs)

        if result is None:
            continue

        results.extend(result)

    return results


@add_debug
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
