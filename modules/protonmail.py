import httpx

from squiz.types import Email
from squiz.abc import BaseModule, BaseModel


class ProtonMailResponse(BaseModel):
    email: str
    exists: bool

    render_fields: dict[str, str] = {"Email": "email", "Exists": "exists"}


class Module(BaseModule):
    name = "ProtonMail check"
    target_types = (Email,)

    def execute(self, **kwargs):
        email = kwargs["target"]

        response = httpx.get(
            f"https://api.protonmail.ch/pks/lookup?op=index&search={email}"
        )

        if response.status_code == 429:
            return

        data = response.text

        self < ProtonMailResponse(email=email.value, exists="info:1:1" in data)
