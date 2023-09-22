import pathlib


def get():
    with open(
        pathlib.Path(__file__).parent.parent.resolve() / "../requirements.txt"
    ) as f:
        return f.read().splitlines()
