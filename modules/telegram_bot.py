import httpx

from squiz.types import TelegramBotToken
from squiz.abc import BaseModule, BaseModel


class TelegramResponse(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    username: str

    render_fields = {
        "ID": "id",
        "Bot?": "is_bot",
        "Profile name": "first_name",
        "Username": "username",
    }


class Module(BaseModule):
    name = "TelegramBotData"
    target_types = (TelegramBotToken,)

    def execute(self, **kwargs):
        response = httpx.get(
            f"https://api.telegram.org/bot{kwargs['target']}/getMe"
        ).json()

        with self.ignore():
            self < TelegramResponse(**response["result"])
