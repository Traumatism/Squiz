import re

from squiz.abc import BaseType


class IPAddress(BaseType[str]):
    """IPAddress type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        return (
            re.fullmatch(
                r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}"
                r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
                value,
            )
            is not None
        )
