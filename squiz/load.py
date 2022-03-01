import importlib
import pkgutil
import inspect
import glob
import os

from typing import Generator

from .base import BaseModule
from .types import ModuleType

PY_MODULES_PATH = "squiz.modules"


def load_modules(
    path: str = os.path.join("squiz", "modules")
) -> Generator[ModuleType, None, None]:
    """ Load all modules """
    for i in os.listdir(path):
        if i.startswith("__"):
            continue

        if i.endswith(".py"):
            module = i.replace(".py", "")
            yield from load_module(
                f"{'.'.join(path.split(os.path.sep))}.{module}"
            )

        else:
            _path = os.path.join(path, i)
            if os.path.isdir(_path):
                yield from load_modules(_path)


def load_module(module: str) -> Generator[ModuleType, None, None]:
    """ Load all modules """

    _module = importlib.import_module(module)

    for _, cls in inspect.getmembers(_module):
        if (
            inspect.isclass(cls)
            and cls != BaseModule
            and not isinstance(cls, BaseModule)
            and issubclass(cls, BaseModule)
        ):
            yield cls
