import json


def pretty(obj: dict) -> str:
    try:
        return json.dumps(
            obj,
            ensure_ascii=False,
            sort_keys=True,
            indent=4
        )
    except:
        return obj


def to_dict(s: str) -> dict:
    try:
        return json.loads(s)
    except:
        return s
