import httpx

from squiz.types import IPAddress, Domain
from squiz.abc import BaseModule, BaseModel


class ProtonVPNResponse(BaseModel):
    target: str
    proton: bool

    render_fields = {"IP/Domain": "target", "Proton?": "proton"}


class Module(BaseModule):
    name = "ProtonVPN check"
    target_types = (IPAddress, Domain)

    def execute(self, **kwargs):
        response = httpx.get(f"https://api.protonmail.ch/vpn/logicals")
        json_data = response.json()
        target = kwargs["target"].value

        found = False

        for logical_server in json_data["LogicalServers"]:
            for server in logical_server["Servers"]:
                if target in (server["EntryIP"], server["ExitIP"], server["Domain"]):
                    found = True
                    break

        self < ProtonVPNResponse(target=target, proton=found)
