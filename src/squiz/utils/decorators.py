import typing

from squiz.logger import Logger


def add_debug(func: typing.Callable) -> typing.Callable:
    """ Add a logger to a function """

    def wrapper(*args, **kwargs) -> None:
        _args = ''.join(map(str, args))
        Logger.debug(f"Executing {func.__name__} with args: {_args}")
        return func(*args, **kwargs)

    return wrapper
