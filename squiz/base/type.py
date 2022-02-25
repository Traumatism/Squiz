import abc

from rich.console import RenderableType


class BaseType(metaclass=abc.ABCMeta):
    """ Base class for all types """

    def __init__(self, value) -> None:
        super().__init__()

        self.__value = value

        if not self.__class__.validate(value):
            raise ValueError(f"Invalid value: {value}")

    @abc.abstractclassmethod
    def validate(cls) -> None:
        """ Validate the type """
        raise NotImplementedError

    @property
    def value(self) -> str:
        """ Get the value """
        return self.__value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} value={self.value}>"

    def __rich__(self) -> RenderableType:
        return f"[green]{self.value}[/green]"
