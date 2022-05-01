import re

from squiz.abc import BaseType


class DiscordToken(BaseType):
    """Discord token type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the Discord token"""
        return (
            re.fullmatch(
                r"^([\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84})$", value
            )
            is not None
        )
