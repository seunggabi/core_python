import os
from configparser import ConfigParser

from seunggabi_core_python.const import DEFAULT, CREDENTIALS
from seunggabi_core_python.exception.bad_request import BadRequest


class Config:
    @staticmethod
    def home():
        return os.path.expanduser("~")

    @staticmethod
    def path(
        group: str = None,
        context: str = None,
    ):
        return f".{group}/{context}"

    @staticmethod
    def get(
        group: str = None,
        context: str = None,
        profile: str = None,
    ) -> dict:
        if group is None or context is None:
            raise BadRequest()

        profile = profile or DEFAULT

        config = ConfigParser()
        config.read(f"{Config.home()}/{Config.path(group, context)}")

        return config._sections[profile]


if __name__ == '__main__':
    print(
        Config.get(
            group="upbit",
            context=CREDENTIALS,
        )
    )
