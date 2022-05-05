from rich.console import Console
from rich.panel import Panel
from rich.box import HEAVY

from typing import Iterable

from squiz import __version__

console = Console()

DEBUG = 0


class Logger:
    """Squiz logger module"""

    @staticmethod
    def print_banner() -> None:
        """Print the ASCII art banner"""

        console.print(
            r"""[yellow]
     __
   [orange3]<[/]([white]o[/] )___  [green]Squiz framework v %s[/]
    ( ._> /  [green]made with luv by @toastakerman[/]
     `---'

            """
            % __version__
        )

    @classmethod
    def log(
        cls,
        message: str,
        color: str,
        title: str,
    ) -> None:
        """Logs a message to the console"""
        console.print(f"[bold {color}]{title}[/] [bold]{message}[/]")

    @classmethod
    def pretty_dict(cls, d: dict) -> Panel:
        """Render a dict as a rich object"""

        def f() -> Iterable[str]:
            """Render the model as a string with 'key : value'"""
            max_len = max(map(len, d.keys()))

            for key, value in d.items():

                if not value:
                    continue

                yield (f"{key:<{max_len}} : {value}\n")

        return Panel.fit(
            "".join(f()),
            border_style="bright_black",
            box=HEAVY,
        )

    @classmethod
    def error(cls, message: str) -> None:
        """Logs an error to the console"""
        cls.log(message, "red", "->")

    @classmethod
    def warning(cls, message: str) -> None:
        """Logs a warning to the console"""
        cls.log(message, "yellow", "->")

    @classmethod
    def info(cls, message: str) -> None:
        """Logs an info to the console"""
        cls.log(message, "blue", "->")

    @classmethod
    def success(cls, message: str) -> None:
        """Logs a success to the console"""
        cls.log(message, "green", "->")

    @classmethod
    def debug(cls, message: str) -> None:
        """Logs a debug to the console"""
        cls.log(message, "cyan", "->") if DEBUG else ...

    @classmethod
    def fatal(cls, message: str) -> None:
        """Logs a fatal to the console"""
        cls.log(message, "red", "->")
