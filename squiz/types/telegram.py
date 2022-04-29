import re

from squiz.base import BaseType


class TelegramBotToken(BaseType):
    """Telegram bot token type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        return (
            re.fullmatch(r"^[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+$", value) is not None
        )
