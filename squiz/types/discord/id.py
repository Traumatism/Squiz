import re

from squiz.abc import BaseType


class DiscordID(BaseType):
    """Discord ID type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the Discord ID"""
        return re.fullmatch(r"^\d{18}$", value) is not None
