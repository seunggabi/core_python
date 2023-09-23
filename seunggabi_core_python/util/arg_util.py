from argparse import ArgumentParser
from typing import Any


class Argument:
    def __init__(
        self,
        name: str,
        short: str = None,
        default: str = None,
        help: str = None,
        is_param: str = True,
    ):
        self.name = name
        self.short = short or name[0:1]

        self.default = default
        self.help = help
        self.is_param = is_param

    @staticmethod
    def make(config) -> list:
        return [Argument(**x) for x in config]


def make(config: list = None) -> Any:
    args = Argument.make(config)

    usage = [
        "Usage: python3",
        __file__,
    ]
    for i in args:
        usage.append(f"[--{i.name} <{i.name}>]")

    arg_parser = ArgumentParser(usage=" ".join(usage))

    for i in args:
        arg_parser.add_argument(
            f"-{i.short}",
            f"--{i.name}",
            default=i.default,
            help=(i.help or i.name),
        )

    return arg_parser.parse_args(), args
