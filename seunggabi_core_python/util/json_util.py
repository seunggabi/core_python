import json
from typing import Union


def pretty(obj: Union[dict, str]) -> str:
    try:
        if isinstance(obj, str):
            obj = to_dict(obj)

        return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=4)
    except:
        return obj


def to_dict(s: str) -> dict:
    try:
        return json.loads(s)
    except:
        try:
            return json.loads(json.dumps(eval(s)))
        except:
            return s


def to_dict_with_attr(s: str) -> dict:
    d = to_dict(s)

    o = JsonObject()
    for k, v in d.items():
        setattr(o, k, v)

    return o


class JsonObject:
    pass
