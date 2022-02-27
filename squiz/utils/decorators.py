from typing import Callable

from squiz.logger import Logger


def debug(func: Callable) -> Callable:
    """ Add a debug logger to a function """

    def wrapper(*args, **kwargs) -> None:
        _args = ''.join(map(str, args))
        Logger.debug(f"Executing {func.__name__} with args: {_args}")
        return func(*args, **kwargs)

    return wrapper
