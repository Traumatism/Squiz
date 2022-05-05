import httpx

from typing import Optional

from squiz.types import IPAddress
from squiz.abc import BaseModule, BaseModel


class IPInfo(BaseModel):
    ip: str
    hostname: Optional[str]
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str

    render_fields = {
        "IP Address": "ip",
        "City": "city",
        "Region": "region",
        "Country": "country",
        "Location": "loc",
        "Organization": "org",
        "Postal Code": "postal",
    }


class Module(BaseModule):

    name = "IPInfo"
    target_types = (IPAddress,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = httpx.get(f"https://ipinfo.io/{target}/json")

        try:
            self.results.append(IPInfo(**response.json()))
        except Exception:
            return
