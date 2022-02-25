import argparse
import squiz.types

from typing import Optional


from squiz.load import load_modules
from squiz.base import BaseType
from squiz.logger import Logger


def parse_target(target: str) -> Optional[BaseType]:
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

    modules = filter(
        lambda x: target.__class__ in x.target_types,
        load_modules()
    )

    Logger.success("Loaded modules !")

    conf = {"target": target}

    Logger.info("Running modules...")

    for module in modules:
        module()._execute(**conf)

    Logger.success("Done !")
