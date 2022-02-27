import re

from ..base import BaseType


class Username(BaseType):
    """ Username type """

    @classmethod
    def validate(cls, value) -> bool:
        """ Validate the type """
        return re.fullmatch(r"^\w{3,16}$", value) is not None
