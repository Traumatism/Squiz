import requests

from squiz.types import UUID, Username
from squiz.base import BaseModule, BaseModel


class UsernameToUUID(BaseModel):
    id: str
    name: str

    render_fields = {
        "Username": "name",
        "UUID": "uuid"
    }

    @property
    def uuid(self) -> UUID:
        return UUID(self.id)


class Module(BaseModule):

    name = "Mojang"
    target_types = (Username, )

    def execute(self, **kwargs) -> None:
        target = kwargs["target"]

        response = requests.get(
            f"https://api.mojang.com/users/profiles/minecraft/{target}"
        )

        data = UsernameToUUID(**response.json())

        self.results.append(data)
