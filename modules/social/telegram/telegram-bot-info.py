import httpx

from typing import Optional

from squiz.abc import BaseModel, BaseModule
from squiz.types import TelegramBotToken


class TelegramBotInfo(BaseModel):
    id: int
    first_name: str
    username: Optional[str]

    render_fields = {"ID": "id", "Name": "first_name", "Username": "username"}


class Module(BaseModule):
    name = "Telegram infos"
    target_types = (TelegramBotToken,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = httpx.get(f"https://api.telegram.org/bot{target}/getMe")

        try:
            self.results.append(TelegramBotInfo(**response.json()["result"]))
        except Exception:
            return
