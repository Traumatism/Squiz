import re

from squiz.abc import BaseType


class UUID(BaseType):
    """UUID type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        match = re.fullmatch(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
            r"|^[0-9a-f]{32}$",
            value,
        )

        return match is not None

    @property
    def value(self) -> str:
        """Get the value"""
        val = super().value

        return (
            (f"{val[:8]}-{val[8:12]}-{val[12:16]}-{val[16:20]}-{val[20:32]}")
            if len(val) == 32
            else val
        )
