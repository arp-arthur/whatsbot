class CustomException(Exception):
    name: str
    code: int
    msg: str

class CustomHTTPException(CustomException):
    _msg = "A violation happened. The request is corrupted. The admin have been noticed."
    code = 500

    def __init__(self) -> None:
        self.msg = self._msg
        super().__init__(self.msg)

