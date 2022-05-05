from .email import Email
from .ipaddress import IPAddress
from .uuid import UUID
from .username import Username
from .url import URL
from .discord.token import DiscordToken
from .discord.id import DiscordID
from .telegram import TelegramBotToken
from .port import Port
from .domain import Domain

types = (
    Email,
    IPAddress,
    UUID,
    Username,
    URL,
    TelegramBotToken,
    DiscordToken,
    DiscordID,
    Port,
    Domain,
)
