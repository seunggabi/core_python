import json


def pretty(obj):
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        indent=4
    )
