import re
import contextlib

import pydantic

from abc import abstractmethod, ABC

from rich.table import Table
from rich.console import RenderableType

from typing import Iterable, final, Generic, TypeVar


class BaseModel(pydantic.BaseModel):
    """Pydantic on steroids"""

    render_fields: dict[str, str]

    @final
    def dump(self) -> dict:
        """Dump model to JSON"""
        return {attr: getattr(self, attr) for attr in self.render_fields.values()}

    @final
    def __rich__(self) -> Table:
        """Render the model as a rich object"""

        def f() -> Iterable[tuple[str, str]]:
            """Render the model as a string with 'key : value'"""

            for key, value in self.render_fields.items():
                if (value := getattr(self, value)) is None:
                    continue

                if isinstance(value, list):
                    value = ", ".join(value)

                if isinstance(value, bool):
                    value = "Yep :3" if value else "Nup >:o"
                    key += "?" if not key.endswith("?") else ""

                yield str(key), str(value)

        table = Table(show_header=False, border_style="bright_black")

        for k, v in f():
            table.add_row(k, v)

        return table


T = TypeVar("T")


class BaseType(ABC, Generic[T]):
    """Base class for all types"""

    @final
    def __init__(self, value: T, raise_exc: bool = True) -> None:
        super().__init__()

        self.__value = value

        if not self.__class__.validate(value) and raise_exc:
            raise ValueError(f"Invalid value: {value}")

    @classmethod
    @abstractmethod
    def validate(cls, value) -> bool:
        """Validate the type"""

    @property
    def value(self) -> T:
        """Get the value"""
        return self.__value

    @final
    def __str__(self) -> str:
        return str(self.value)

    @final
    def __rich__(self) -> RenderableType:
        return f"[green]{self.value}[/green]"

    @staticmethod
    def from_regex(regex: str):
        """Create a type that validates the given regular expression"""

        class Aux(BaseType):
            """Auxiliary class"""

            @classmethod
            def validate(cls, value: str):
                return re.fullmatch(regex, value) is not None

        return Aux


class BaseModule(ABC):
    """Base class for all modules"""

    name: str
    target_types: Iterable[type[BaseType]]
    active: bool = False

    @final
    def __init__(self) -> None:
        """Initialize the module"""
        self.ignore = contextlib.suppress
        self.results: list[BaseModel] = list()

        self.env: dict[str, str] = {}

        with open(".env") as f:
            content: str = f.read()

            for line in content.splitlines():
                kv_pair = line.split("=", 1)

                self.env[kv_pair[0]] = kv_pair[1]

        super().__init__()

    @abstractmethod
    def execute(self, **kwargs):
        """Run the module"""

    @final
    def __lt__(self, op: BaseModel):
        self.results.append(op)
