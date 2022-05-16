import contextlib
import httpx

from squiz.types import UUID, Username
from squiz.abc import BaseModule, BaseModel


class UsernameToUUID(BaseModel):
    id: str
    name: str

    render_fields = {"Username": "name", "UUID": "uuid"}

    @property
    def uuid(self) -> UUID:
        return UUID(self.id)


class Module(BaseModule):

    name = "Mojang"
    target_types = (Username,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = httpx.get(
            f"https://api.mojang.com/users/profiles/minecraft/{target}"
        )

        with contextlib.suppress():
            self.results.append(UsernameToUUID(**response.json()))
