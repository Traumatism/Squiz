import requests
import typing

from squiz.types import IPAddress
from squiz.base import BaseModule, BaseModel


class ShodanResponse(BaseModel):

    ip: str
    ports: typing.List[int]
    tags: typing.List[str]
    hostnames: typing.List[str]
    cpes: typing.List[str]
    vulns: typing.List[str]

    render_fields = {
        "IP Address": "ip",
        "Ports": "ports_str",
        "Tags": "tags_str",
        "Hostnames": "hostnames_str",
        "CPEs": "cpes_str",
        "Vulnerabilities": "vulns_str"
    }

    @property
    def tags_str(self) -> str:
        return ", ".join(self.tags)

    @property
    def ports_str(self):
        return ", ".join(map(str, self.ports))

    @property
    def hostnames_str(self):
        return ", ".join(self.hostnames)

    @property
    def vulns_str(self):
        return ", ".join(self.vulns)

    @property
    def cpes_str(self):
        return ", ".join(self.cpes)


class Module(BaseModule):

    name = "Shodan"
    target_types = (IPAddress, )

    def execute(self, **kwargs):
        target = kwargs["target"]
        response = requests.get(f"https://internetdb.shodan.io/{target}")

        try:
            self.results.append(ShodanResponse(**response.json()))
        except Exception:
            return
