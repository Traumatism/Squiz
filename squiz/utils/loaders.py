import os

from inspect import getmembers, isclass
from importlib import import_module

from typing import Iterable, Type

from squiz.abc import BaseModule

BaseModuleType = Type[BaseModule]


def load_modules(path: str = "modules") -> Iterable[BaseModuleType]:
    """Load all modules"""

    for i in os.listdir(path):
        if i.startswith("__"):
            continue

        elif i.endswith(".py"):
            yield from load_module(
                f'{".".join(path.split(os.path.sep))}' "." f'{i.removesuffix(".py")}'
            )

        else:
            if os.path.isdir(new_path := os.path.join(path, i)):
                yield from load_modules(new_path)


def load_module(module: str) -> Iterable[BaseModuleType]:
    """Load a module"""

    for _, cls in getmembers(import_module(module)):
        if isinstance(cls, BaseModule) or cls == BaseModule:
            continue

        if isclass(cls) and issubclass(cls, BaseModule):
            yield cls
