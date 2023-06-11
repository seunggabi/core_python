class BadRequest(Exception):
    def __init__(self):
        super().__init__("400 BAD REQUEST")
