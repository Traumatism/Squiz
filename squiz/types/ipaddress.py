import re

from squiz.base import BaseType


class IPAddress(BaseType):
    """ IPAddress type """

    @classmethod
    def validate(cls, value) -> bool:
        """ Validate the type """
        return re.fullmatch(
            r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", value
        ) is not None
