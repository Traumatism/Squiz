import pydantic

from rich.console import RenderableType


class BaseModel(pydantic.BaseModel):
    """ Base class for all pydantic models, rich support """

    render_fields = {}

    def __rich__(self) -> RenderableType:
        """ Render the model as a rich object """

        max_key_len = max(len(key) for key in self.render_fields.keys())

        return "".join(
            f"{key:<{max_key_len}} : {getattr(self, value) or 'n/a'}\n"
            for key, value in self.render_fields.items()
            if getattr(self, value) is not None
        )
