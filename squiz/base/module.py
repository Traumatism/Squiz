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

    @abc.abstractmethod
    def execute(self, **kwargs) -> typing.Optional[State]:
        """ Execute the module """
        raise NotImplementedError(
            f"execute() not implemented for module: {self.name}"
        )
