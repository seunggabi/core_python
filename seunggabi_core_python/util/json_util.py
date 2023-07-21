import json


def pretty(obj: dict) -> str:
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        indent=4
    )


def to_dict(s: str) -> dict:
    return json.loads(s)
