from .ipaddress import IPAddress
from .uuid import Uuid
from .port import Port

from ..abc import BaseType

Domain = BaseType.from_regex(
    r"^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$"
)

DiscordToken = BaseType.from_regex(r"^([\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84})$")
DiscordID = BaseType.from_regex(r"^\d{18}$")
Url = BaseType.from_regex(r"^https?://.+$")
TelegramBotToken = BaseType.from_regex(r"^[a-zA-Z0-9-_]+:[a-zA-Z0-9-_]+$")
Username = BaseType.from_regex(r"^([a-zA-Z0-9_]{3,16})$")
Email = BaseType.from_regex(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


types = (
    Email,
    IPAddress,
    Uuid,
    Username,
    Url,
    TelegramBotToken,
    DiscordToken,
    Domain,
    DiscordID,
    Port,
)
