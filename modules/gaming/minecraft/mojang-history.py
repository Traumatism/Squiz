import time
import httpx
import contextlib

from typing import Optional

from squiz.types import UUID
from squiz.abc import BaseModule, BaseModel


class UUIDToNameHistory(BaseModel):
    name: str
    changedToAt: Optional[int]
    render_fields = {"Username": "name", "Change date": "date"}

    @property
    def date(self) -> str:
        """Get the date"""
        return (
            time.strftime(
                "[green]%Y-%m-%d[/green]",
                time.localtime((self.changedToAt // 1000) + 1),
            )
            if self.changedToAt is not None
            else "[red]First username[/red]"
        )


class Module(BaseModule):
    name = "Mojang-history"
    target_types = (UUID,)

    def execute(self, **kwargs):
        target = kwargs["target"]

        response = httpx.get(f"https://api.mojang.com/user/profiles/{target}/names")

        for row in response.json():
            with contextlib.suppress():
                self.results.append(UUIDToNameHistory(**row))
