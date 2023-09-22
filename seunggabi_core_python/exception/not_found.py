class NotFound(Exception):
    def __init__(self, msg: str = ""):
        super().__init__(f"[404 NOT_FOUND] {msg}")
