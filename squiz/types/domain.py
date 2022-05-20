import re

from squiz.abc import BaseType


class Domain(BaseType):
    """Domain name type"""

    @classmethod
    def validate(cls, value) -> bool:
        """Validate the type"""

        domain_regex = (
            r"^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$"
        )

        return re.fullmatch(domain_regex, value) is not None
