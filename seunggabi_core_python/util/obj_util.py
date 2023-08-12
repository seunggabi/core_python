def safe_get(
    obj: dict,
    key: str,
    default=None,
    force_key_str=False,
):
    try:
        for k in key.split("."):
            if not force_key_str:
                try:
                    k = int(k)
                except:
                    pass

            obj = obj[k]

        return default if obj is None else obj
    except:
        return default


if __name__ == '__main__':
    obj = {
        "a": 1,
        "z": {
            "b": 0
        }
    }
    print(safe_get(obj, "a"))
    print(safe_get(obj, "b"))
    print(safe_get(obj, "b", 3))
    print(safe_get(obj, "z.b"))
