from .email import Email
from .ipaddress import IPAddress
from .uuid import UUID
from .username import Username
from .url import URL
from .discord import DiscordToken
from .telegram import TelegramBotToken
from .port import Port

types = (
    Email,
    IPAddress,
    UUID,
    Username,
    URL,
    TelegramBotToken,
    DiscordToken,
    Port,
)
