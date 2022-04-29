import re

from ..base import BaseType


class URL(BaseType):
    """URL type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""
        return re.fullmatch(r"^https?://.+$", value) is not None
