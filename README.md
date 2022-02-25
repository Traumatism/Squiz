# Squiz
## 🔎  OSINT Framework

## 📝 Documentation

### Add a new module

    * Create a new Python file in the `modules/` directory
    * See next code for details
```py
import requests

from squiz.base import BaseModule, BaseModel
from squiz.types import Username


class Row(BaseModel):
    var1: str
    var2: Optional[int] = None

    render_fields = {
        "Name 1": "var1",
        "Name 2": "p1"
    }

    @property
    def p1(self):
        return "null" if self.var2 is None else self.var2


class Module(BaseModule):

    name = "Sample"
    target_types = (Username, )  # Target type(s)

    def execute(self, **kwargs) -> None:
        target = kwargs["target"]

        # Do something with target
        response: requests.Response = request.get(...)

        self.results.add(Row(**response.json()))
```
