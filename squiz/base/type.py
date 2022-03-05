from abc import ABCMeta, abstractclassmethod
from rich.console import RenderableType


class BaseType(metaclass=ABCMeta):
    """ Base class for all types """

    def __init__(self, value, raise_exc=True) -> None:
        super().__init__()

        self.__value = value

        if not self.__class__.validate(value) and raise_exc is True:
            raise ValueError(f"Invalid value: {value}")

    @abstractclassmethod
    def validate(cls) -> bool:
        """ Validate the type """
        raise NotImplementedError

    @property
    def value(self) -> str:
        """ Get the value """
        return self.__value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"value={self.value} valid={self.validate}>"
        )

    def __rich__(self) -> RenderableType:
        return f"[green]{self.value}[/green]"
