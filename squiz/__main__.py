import typing
import squiz.types
import rich_click as click

from squiz.logger import Logger
from squiz.load import load_modules
from squiz.base import BaseType, BaseModule
from squiz.utils.executors import execute_many

click.rich_click.USE_RICH_MARKUP = True


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


@click.group()
def cli(): ...


@cli.command()
@click.argument("target", required=True)
def main(target):
    Logger.print_banner()

    target = parse_target(target)

    if not target:
        return

    modules = get_modules(target)

    if not modules:
        return

    execute_many(modules, **{"target": target})


if __name__ == "__main__":
    main()
