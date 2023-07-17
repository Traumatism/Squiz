import httpx

from squiz.types import IPAddress
from squiz.abc import BaseModule, BaseModel


class IPInfoResponse(BaseModel):
    ip: str
    hostname: str | None
    anycast: bool | None
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str
    timezone: str

    render_fields: dict[str, str] = {
        "IP Address": "ip",
        "Hostname": "hostname",
        "City": "city",
        "Region": "region",
        "Country": "country",
        "Lat/Lon": "loc",
        "Organisation": "org",
        "Postal": "postal",
        "Timezone": "timezone",
    }


class Module(BaseModule):
    name = "IPInfo"
    target_types = (IPAddress,)

    def execute(self, **kwargs):
        with self.ignore():
            self < IPInfoResponse(
                **httpx.get(f"https://ipinfo.io/{kwargs['target']}/json").json()
            )
