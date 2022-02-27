import re

from ..base import BaseType


class Email(BaseType):
    """ Email type """

    @classmethod
    def validate(cls, value) -> bool:
        """ Validate the type """
        return re.fullmatch(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value
        ) is not None
