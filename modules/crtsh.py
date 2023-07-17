import httpx

from squiz.types import IPAddress, Domain, Email
from squiz.abc import BaseModule, BaseModel


class Row(BaseModel):
    issuer_ca_id: int
    name_value: str
    issuer_name: str
    common_name: str

    render_fields: dict[str, str] = {
        "Issuer CA ID": "issuer_ca_id",
        "Issuer name": "issuer_name",
        "Common name": "common_name",
        "Name": "name_value",
    }


class Module(BaseModule):
    name = "CrtSH lookup"
    target_types = (IPAddress, Domain, Email)

    def execute(self, **kwargs):
        response = httpx.get(f"https://crt.sh/?q={kwargs['target']}&output=json")

        for data in response.json():
            self < Row(**data)

        return super().execute(**kwargs)
