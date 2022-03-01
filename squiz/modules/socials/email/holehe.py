import trio
import httpx

from typing import Optional

from squiz.base import BaseModule, BaseModel
from squiz.types import Email

from holehe.core import get_functions, launch_module, import_submodules


class HoleheOutput(BaseModel):
    name: str
    domain: str
    phoneNumber: Optional[str]
    exists: bool

    render_fields = {
        "Name": "name",
        "Domain": "domain",
        "Phone Number": "phoneNumber",
        "Exists": "exists"
    }


class Module(BaseModule):
    name = "holehe"
    target_types = (Email, )

    async def run(self):

        client = httpx.AsyncClient()
        modules = import_submodules("holehe.modules")
        functions = get_functions(modules)

        results = []

        async with trio.open_nursery() as nursery:
            for func in functions:
                nursery.start_soon(
                    launch_module, func, self.target, client, results
                )

        await client.aclose()

        for result in results:
            if result.get("exists"):
                self.results.append(HoleheOutput(**result))

    def execute(self, **kwargs):
        self.target = kwargs["target"]
        trio.run(self.run)
