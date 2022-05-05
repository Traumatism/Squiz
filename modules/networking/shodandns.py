import dotenv
import httpx
import os

from squiz.abc import BaseModule, BaseModel
from squiz.types import Domain


class DomainRow(BaseModel):
    full: str
    type: str
    value: str
    last_seen: str

    render_fields = {
        "Subdomain": "full",
        "Type": "type",
        "Value": "value",
        "Last seen": "last_seen",
    }


class Shodan(BaseModule):

    name = "ShodanDNS"
    target_types = (Domain,)

    def execute(self, **kwargs):
        target = kwargs["target"].value

        dotenv.load_dotenv()
        params = {"key": os.environ["SHODAN_API_KEY"]}

        response = httpx.get(
            f"https://api.shodan.io/dns/domain/{target}",
            params=params,
        )

        if response.status_code != 200:
            return

        for row in response.json()["data"]:
            row["full"] = row["subdomain"] + "." + target
            self.results.append(DomainRow(**row))
