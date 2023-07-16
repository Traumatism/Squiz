from rich.console import Console

from squiz import __version__

console = Console()

DEBUG = 0


class Logger:
    """Squiz logger module"""

    @staticmethod
    def print_banner() -> None:
        """Print the ASCII art banner"""

        console.print(
            """

        (o)[bright_black],
 [cyan]~ ~ ~ ~[/] | | [cyan]~ ~ ~ ~ ~[/]
         | |                [bold red]Squiz Framework[/]
  .------| |----,
 (  [yellow]o o o o[/yellow]  __/[white]  *   *[/]     [blue italic]github.com/traumatism[/]
  '-._______':@ [white]*  *[/]
[/]
            """
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
    def error(cls, message: str) -> None:
        """Logs an error to the console"""
        cls.log(message, "red", "!")

    @classmethod
    def warning(cls, message: str) -> None:
        """Logs a warning to the console"""
        cls.log(message, "yellow", "^")

    @classmethod
    def info(cls, message: str) -> None:
        """Logs an info to the console"""
        cls.log(message, "blue", "~")

    @classmethod
    def success(cls, message: str) -> None:
        """Logs a success to the console"""
        cls.log(message, "green", "+")

    @classmethod
    def debug(cls, message: str) -> None:
        """Logs a debug to the console"""
        cls.log(message, "cyan", "D") if DEBUG else ...

    @classmethod
    def fatal(cls, message: str) -> None:
        """Logs a fatal to the console"""
        cls.log(message, "red", "!!!")
