class NotOk(Exception):
    def __init__(self, msg: str = ""):
        super().__init__(f"[!200 NOT_OK] {msg}")
