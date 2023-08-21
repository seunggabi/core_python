import json
from typing import Union


def pretty(obj: Union[dict, str]) -> str:
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
        return json.loads(
            json.dumps(
                eval(s)
            )
        )
