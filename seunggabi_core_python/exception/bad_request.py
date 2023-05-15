class BadRequest(Exception):
    def __init__(self):
        super().__init__("404 NOT_FOUND")
