import os
import re


def read(name: str) -> str:
    with open(name) as file:
        lines = [line.rstrip() for line in file]

        return "\n".join(lines)


def name(
    path: str,
    regexp: str,
) -> list:
    pattern = re.compile(regexp)

    return sorted([x for x in os.listdir(path) if pattern.search(x)])


def read_all(
    path: str,
    regexp: str,
) -> dict:
    o = {}
    for i in name(path, regexp):
        o[i] = read(f"{path}/{i}")

    return o
