import requests

from typing import Optional

from squiz.base import BaseModel, BaseModule
from squiz.types import DiscordToken


class DiscordInfo(BaseModel):
    id: int
    avatar: str
    username: str
    discriminator: int
    phone: Optional[str]
    email: Optional[str]
    verified: bool
    mfa_enabled: bool
    locale: str

    render_fields = {
        "ID": "id",
        "Username": "username",
        "Discriminator": "discriminator",
        "Avatar": "avatar",
        "Phone": "phone",
        "Email": "email",
        "Verified": "verified",
        "MFA": "mfa_enabled",
        "Locale": "locale"
    }


class Module(BaseModule):
    name = "Discord infos"
    target_types = (DiscordToken, )

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = requests.get(
            "https://discordapp.com/api/v6/users/@me",
            headers={"Authorization": target.value}
        )

        try:
            self.results.append(DiscordInfo(**response.json()))
        except Exception:
            return self.ExecutionError("Invalid response")

        return self.ExecutionSuccess()
