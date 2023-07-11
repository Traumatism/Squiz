import pydantic

from abc import ABC, abstractmethod

from rich.box import ASCII2
from rich.table import Table
from rich.console import RenderableType

from typing import Iterable, Type, final


class BaseModel(pydantic.BaseModel):
    """Base class for all pydantic models, rich support"""

    render_fields = {}

    def __rich__(self) -> RenderableType:
        """Render the model as a rich object"""

        def f() -> Iterable[tuple[str, str]]:
            """Render the model as a string with 'key : value'"""

            for key, value in self.render_fields.items():
                value = getattr(self, value)

                if not value:
                    continue

                yield str(key), str(value)

        table = Table(box=ASCII2, show_header=False, border_style="bright_black")

        for k, v in f():
            table.add_row(k, v)

        return table


class BaseType(ABC):
    """Base class for all types"""

    def __init__(self, value, raise_exc=True) -> None:
        super().__init__()

        self.__value = value

        if not self.__class__.validate(value) and raise_exc is True:
            raise ValueError(f"Invalid value: {value}")

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        raise NotImplementedError

    @property
    def value(self):
        """Get the value"""
        return self.__value

    def __str__(self) -> str:
        return str(self.value)

    def __rich__(self) -> RenderableType:
        return f"[green]{self.value}[/green]"


class BaseModule(ABC):
    """Base class for all modules"""

    name: str
    target_types: Iterable[Type[BaseType]]

    @final
    def __init__(self) -> None:
        """Initialize the module"""
        super().__init__()

        self.results: list[BaseModel] = list()

    @abstractmethod
    def execute(self, **kwargs):
        """Execute the module"""
