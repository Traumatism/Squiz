import contextlib
import httpx
import time

from squiz.abc import BaseModule, BaseModel
from squiz.types import Username


class KeybaseBasics(BaseModel):
    username: str
    ctime: int

    render_fields = {"Username": "username", "Created": "ctime"}

    @property
    def ctime_date(self) -> str:
        """Get the date"""
        FMT = "[green]%Y-%m-%d[/green]"
        return time.strftime(FMT, time.localtime(self.ctime))


class KeybaseProfile(BaseModel):
    full_name: str
    location: str
    bio: str

    render_fields = {
        "Full name": "full_name",
        "Location": "location",
        "Bio": "bio",
    }


class Module(BaseModule):
    name = "Keybase"
    target_types = (Username,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = httpx.get(
            "https://keybase.io/_/api/1.0/user/lookup.json",
            params={"username": target.value},
        )

        with contextlib.suppress(Exception):
            json_data = response.json()["them"]["profile"]
            self.results.append(KeybaseProfile(**json_data))

        with contextlib.suppress(Exception):
            json_data = response.json()["them"]["basics"]
            self.results.append(KeybaseBasics(**json_data))
