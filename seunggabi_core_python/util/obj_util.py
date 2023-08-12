def safe_get(
    obj: dict,
    key: str,
    default=None,
):
    k = key.split(".")

    try:
        for i in k:
            obj = obj[i]
        return obj if obj is not None else default
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
