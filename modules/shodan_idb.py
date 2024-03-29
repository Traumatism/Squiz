import httpx

from squiz.types import IPAddress
from squiz.abc import BaseModule, BaseModel


class ShodanIDBResponse(BaseModel):
    ip: str
    ports: list[int]
    tags: list[str]
    hostnames: list[str]
    cpes: list[str]
    vulns: list[str]

    render_fields: dict[str, str] = {
        "IP Address": "ip",
        "Ports": "ports_str",
        "Tags": "tags_str",
        "Hostnames": "hostnames_str",
        "CPEs": "cpes_str",
        "Vulnerabilities": "vulns_str",
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
    name = "Shodan Internet DB"
    target_types = (IPAddress,)

    def execute(self, **kwargs):
        with self.ignore():
            self < ShodanIDBResponse(
                **httpx.get(f"https://internetdb.shodan.io/{kwargs['target']}").json()
            )
