import pydantic

from rich.panel import Panel
from rich.console import RenderableType

from typing import Dict


class BaseModel(pydantic.BaseModel):
    """Base class for all pydantic models, rich support"""

    render_fields = {}  # type: Dict[str, str]

    def __rich__(self) -> RenderableType:
        """Render the model as a rich object"""
        return Panel.fit(
            "".join(
                f"{key:<{max(map(len, self.render_fields.keys()))}}"
                f" : {getattr(self, value) or 'n/a'}\n"
                for key, value in self.render_fields.items()
                if getattr(self, value) is not None
            ),
            border_style="bright_black",
        )
