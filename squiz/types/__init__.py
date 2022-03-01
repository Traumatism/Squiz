from .email import Email
from .ipaddress import IPAddress
from .uuid import UUID
from .username import Username
from .url import URL
from .discord import DiscordToken
from .telegram import TelegramBotToken
from .port import Port

from ..base.type import BaseType
from ..base.model import BaseModel
from ..base.module import BaseModule

from typing import Type

ModuleType = Type[BaseModule]
ModelType = Type[BaseModel]
TypeType = Type[BaseType]

types = [
    Email,
    IPAddress,
    UUID,
    Username,
    URL,
    TelegramBotToken,
    DiscordToken,
    Port
]
