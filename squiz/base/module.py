from abc import abstractmethod, ABCMeta

from typing import Iterable, Type, List

from .type import BaseType
from .model import BaseModel
from ..logger import console, Logger


class BaseModule(Logger, metaclass=ABCMeta):
    """ Base class for all modules """

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
    def execute(self, **kwargs):
        """ Execute the module """
        raise NotImplementedError("execute() not implemented")
