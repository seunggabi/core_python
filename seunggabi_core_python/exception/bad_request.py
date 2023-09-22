class BadRequest(Exception):
    def __init__(self, msg: str = ""):
        super().__init__(f"[400 BAD REQUEST] {msg}")
