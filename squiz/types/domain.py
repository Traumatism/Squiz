import re

from squiz.abc import BaseType


class Domain(BaseType):
    """Domain/Subdomain type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        match = re.fullmatch(
            r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*"
            r"([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$",
            value,
        )

        return match is not None
