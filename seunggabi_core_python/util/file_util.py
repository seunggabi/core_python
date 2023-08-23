import os
import re


def read(filename: str) -> str:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

        return "\n".join(lines)


def count(
    path: str,
    regexp: str,
) -> int:
    pattern = re.compile(regexp)

    count = 0
    for filename in os.listdir(path):
        if pattern.search(filename):
            count += 1

    return count
