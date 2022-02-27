from .email import Email
from .ipaddress import IPAddress
from .uuid import UUID
from .username import Username
from .url import URL

from squiz.base.type import BaseType
from squiz.base.model import BaseModel
from squiz.base.module import BaseModule

from typing import Type

ModuleType = Type[BaseModule]
ModelType = Type[BaseModel]
TypeType = Type[BaseType]

types = [
    Email,
    IPAddress,
    UUID,
    Username,
    URL
]
