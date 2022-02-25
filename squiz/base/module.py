import abc
import typing

from .type import BaseType
from .model import BaseModel

from ..logger import console, Logger


class BaseModule(Logger, metaclass=abc.ABCMeta):
    """ Base class for all modules """

    class State:
        """ Module state """
        def __init__(self, message="") -> None:
            self.message = message

    class ExecutionError(State):
        """ Error while executing the module """

    class ExecutionSuccess(State):
        """ Successful execution of the module """

    name: str
    target_types: typing.Iterable[typing.Type[BaseType]]

    def __init__(self) -> None:
        """ Initialize the module """
        super().__init__()

        self.results: typing.List[BaseModel] = []

    def print(self, *args) -> None:
        """ Pretty rich print """
        console.print(*args)

    def _execute(self, **kwargs) -> None:
        """ Execute the module """

        Logger.debug(f"Executing module: {self.name}")

        try:
            state = self.execute(**kwargs)
        except Exception as e:
            return Logger.error(
                f"Error while executing module {self.name}: {e}"
            )

        if isinstance(state, self.ExecutionSuccess):
            Logger.info(f"Successfully executed module {self.name}")

        if isinstance(state, self.ExecutionError):
            Logger.error(
                f"Potential Error while executing module {self.name}: "
                f"{state.message}"
            )

        if not self.results:
            return

        s = f'Result(s) for module: {self.name}'
        console.print(f"\n[bold white]{s}[/]\n{'-' * len(s)}")

        del s

        for row in self.results:
            console.print(row)

    @abc.abstractmethod
    def execute(self, **kwargs) -> typing.Optional[State]:
        """ Execute the module """
        raise NotImplementedError(
            f"execute() not implemented for module: {self.name}"
        )
