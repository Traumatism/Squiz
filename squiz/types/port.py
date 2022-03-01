import re

from typing import Tuple

from .ipaddress import IPAddress
from ..base import BaseType


class Port(BaseType):
    """ TCP port type """

    @classmethod
    def validate(cls, value) -> bool:
        """ Validate the type """
        return re.fullmatch(
            r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$", value
        ) is not None

    @property
    def value(self) -> Tuple[IPAddress, int]:
        """ Get the value """
        host, port = super().value.split(":")
        return IPAddress(host), int(port)
