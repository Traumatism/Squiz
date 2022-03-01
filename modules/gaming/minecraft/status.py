from typing import Any

from mcstatus import MinecraftServer

from squiz.base import BaseModule, BaseModel
from squiz.types import Port


class MinecraftServerStatus(BaseModel):
    players: str
    version: str
    protocol: int
    description: Any

    render_fields = {
        "Players": "players",
        "Protocol": "protocol",
        "Version": "version",
        "MOTD": "motd"
    }

    @property
    def motd(self) -> str:
        """ Get the MOTD """
        return "".join(
            part.split("'")[0] for part in self.description.split("'text': '")
        )


class Module(BaseModule):
    name = "Minecraft Server Status"
    target_types = (Port, )

    def execute(self, **kwargs):
        host, port = kwargs["target"].value

        try:
            server = MinecraftServer.lookup(f"{host}:{port}")
            status = server.status()

            self.results.append(MinecraftServerStatus(
                players=f"{status.players.online}/{status.players.max}",
                version=status.version.name,
                protocol=status.version.protocol,
                description=status.description
            ))

        except Exception as e:
            self.fatal(str(e))
            return
