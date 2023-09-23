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
