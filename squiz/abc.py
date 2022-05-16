import pydantic

from abc import ABC, abstractmethod

from rich.box import HEAVY
from rich.panel import Panel
from rich.console import RenderableType

from typing import Iterable, Type, List


class BaseModel(pydantic.BaseModel):
    """Base class for all pydantic models, rich support"""

    render_fields = {}  # type: ignore

    def __rich__(self) -> RenderableType:
        """Render the model as a rich object"""

        def f() -> Iterable[str]:
            """Render the model as a string with 'key : value'"""
            max_len = max(map(len, self.render_fields.keys()))

            for key, value in self.render_fields.items():
                value = getattr(self, value)

                if not value:
                    continue

                yield (f"{key:<{max_len}} : {value}\n")

        return Panel.fit(
            "".join(f()),
            border_style="bright_black",
            box=HEAVY,
        )


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

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} " f"value={self.value} valid={self.validate}>"
        )

    def __rich__(self) -> RenderableType:
        return f"[green]{self.value}[/green]"


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
