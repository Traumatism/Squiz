import typing
import argparse
import squiz.types

from squiz.logger import Logger
from squiz.load import load_modules
from squiz.base import BaseType, BaseModule
from squiz.utils.executors import execute_many


def get_modules(target: BaseType) -> typing.Iterable[BaseModule]:
    """ Returns a list of modules that can be executed """
    return map(lambda x: x(), filter(
        lambda x: target.__class__ in x.target_types,
        load_modules()
    ))


def parse_target(target: str) -> typing.Optional[BaseType]:
    """ Parses the target string """
    ts = [
        t for t in squiz.types.types if t.validate(target)
    ]

    if len(ts) == 1:
        return ts[0](target)

    if not ts:
        return Logger.fatal(f"Invalid target: {target}")

    return Logger.fatal(f"Ambiguous target: {target}")


if __name__ == "__main__":
    Logger.print_banner()

    parser = argparse.ArgumentParser(
        description="Squiz - a doxing tool made in Python"
    )

    parser.add_argument(
        "-t", "--target",
        help="Target (username/email/uuid)",
        required=True,
        type=str
    )

    args = parser.parse_args()

    target = parse_target(args.target)

    if target is None:
        exit(0)

    Logger.info(f"Target: {target.value} ({target.__class__.__name__})")

    modules = get_modules(target)

    Logger.success("Loaded modules !")

    Logger.info("Running modules...")

    execute_many(modules, **{"target": target})

    Logger.success("Done !")
