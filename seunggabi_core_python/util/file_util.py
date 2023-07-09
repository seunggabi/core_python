
def read(filename: str) -> str:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

        return "\n".join(lines)


if __name__ == '__main__':
    import os

    path = os.path.dirname(os.path.dirname(__file__))

    print(read(f"{path}/../requirements.txt"))
