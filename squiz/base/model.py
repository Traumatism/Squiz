import pydantic

from typing import Iterable

from rich.panel import Panel
from rich.console import RenderableType


class BaseModel(pydantic.BaseModel):
    """Base class for all pydantic models, rich support"""

    render_fields = {}  # type: ignore

    def __rich__(self) -> RenderableType:
        """Render the model as a rich object"""

        def f() -> Iterable[str]:
            max_len = max(map(len, self.render_fields.keys()))

            for key, value in self.render_fields.items():
                value = getattr(self, value)

                if value is None:
                    continue

                yield (f"{key:<{max_len}} : {value}\n")

        return Panel.fit(
            "".join(f()),
            border_style="bright_black",
        )
