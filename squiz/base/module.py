from abc import ABC, abstractmethod

from typing import Iterable, Type, List

from squiz.base.type import BaseType
from squiz.base.model import BaseModel


class BaseModule(ABC):
    """Base class for all modules"""

    name: str
    target_types: Iterable[Type[BaseType]]

    def __init__(self) -> None:
        """Initialize the module"""
        super().__init__()

        self.results: List[BaseModel] = []

    @abstractmethod
    def execute(self, **kwargs):
        """Execute the module"""
        raise NotImplementedError("execute() not implemented")
