import requests

from squiz.types import IPAddress
from squiz.base import BaseModule, BaseModel


class IPInfo(BaseModel):

    ip: str
    hostname: str
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str

    render_fields = {
        "IP Address": "ip",
        "Hostname": "hostname",
        "City": "city",
        "Region": "region",
        "Country": "country",
        "Location": "loc",
        "Organization": "org",
        "Postal Code": "postal"
    }


class Module(BaseModule):

    name = "IPInfo"
    target_types = (IPAddress, )

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = requests.get(
            f"https://ipinfo.io/{target}/json"
        )

        try:
            self.results.append(IPInfo(**response.json()))
        except Exception:
            return self.ExecutionError("Unexpected JSON response")

        return self.ExecutionSuccess()
