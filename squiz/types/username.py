import re

from squiz.abc import BaseType


class Username(BaseType):
    """Username type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        return re.fullmatch(r"^([a-zA-Z0-9_]{3,16})$", value) is not None
