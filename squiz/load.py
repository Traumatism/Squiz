import importlib
import typing
import pkgutil
import inspect
import os

from squiz.base import BaseModule


PY_MODULES_PATH = "squiz.modules"
OS_MODULES_PATH = [os.path.join(*PY_MODULES_PATH.split("."))]


def load_modules() -> typing.Generator[typing.Type[BaseModule], None, None]:
    """ Load all modules """

    for _, file_name, _ in pkgutil.iter_modules(OS_MODULES_PATH):

        module = importlib.import_module(f"{PY_MODULES_PATH}.{file_name}")

        for _, cls in inspect.getmembers(module):
            if (
                inspect.isclass(cls)
                and cls != BaseModule
                and not isinstance(cls, BaseModule)
                and issubclass(cls, BaseModule)
            ):
                yield cls
