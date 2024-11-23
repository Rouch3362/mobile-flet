class APIException(Exception):
    def __init__(self, error_code: int, error_message: str) -> None:
        self.error_code = error_code
        self.error_message = error_message