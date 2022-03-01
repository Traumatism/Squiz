import os

from inspect import getmembers, isclass
from importlib import import_module

from typing import Generator

from .base import BaseModule
from .types import ModuleType


def load_modules(
    path: str = "modules"
) -> Generator[ModuleType, None, None]:
    """ Load all modules """

    for i in os.listdir(path):

        if i.startswith("__"):
            continue

        if i.endswith(".py"):

            module = (
                f'{".".join(path.split(os.path.sep))}'
                '.'
                f'{i.removesuffix(".py")}'
            )

            yield from load_module(module)

        else:
            new_path = os.path.join(path, i)

            if os.path.isdir(new_path):
                yield from load_modules(new_path)


def load_module(module: str) -> Generator[ModuleType, None, None]:
    """ Load all modules """
    for _, cls in getmembers(import_module(module)):
        if isinstance(cls, BaseModule) or cls == BaseModule:
            continue

        if isclass(cls) and issubclass(cls, BaseModule):
            yield cls
