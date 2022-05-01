import re

from typing import Tuple

from .ipaddress import IPAddress

from squiz.abc import BaseType


class Port(BaseType):
    """TCP port type"""

    @classmethod
    def validate(cls, value) -> bool:  # type: ignore
        """Validate the type (ip:port)"""
        if not isinstance(value, str):
            return False

        if not value.count(":"):
            return False

        ip, port = value.split(":")

        if not IPAddress.validate(ip):
            return False

        if not re.fullmatch(
            r"^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4]"
            r"[0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$",
            port,
        ):
            return False

        return True

    @property
    def value(self) -> Tuple[IPAddress, int]:
        """Get the value"""
        host, port = super().value.split(":")
        return IPAddress(host), int(port)
