def safe_get(
    obj: dict,
    key: str,
    default=None,
):
    return obj[key] if key in obj else default


if __name__ == '__main__':
    obj = {"a": 1}
    print(safe_get(obj, "a"))
    print(safe_get(obj, "b"))
