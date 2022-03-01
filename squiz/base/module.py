from abc import abstractmethod, ABCMeta

from typing import Optional, Iterable, Type, List

from .type import BaseType
from .model import BaseModel
from ..logger import console, Logger


class BaseModule(Logger, metaclass=ABCMeta):
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
    target_types: Iterable[Type[BaseType]]

    def __init__(self) -> None:
        """ Initialize the module """

        super().__init__()
        self.results: List[BaseModel] = []

    def print(self, *args) -> None:
        """ Pretty rich print """
        console.print(*args)

    @abstractmethod
    def execute(self, **kwargs) -> Optional[State]:
        """ Execute the module """
        raise NotImplementedError("execute() not implemented")
