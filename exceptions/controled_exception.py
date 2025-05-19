from werkzeug.http import HTTP_STATUS_CODES
from http import HTTPStatus

class HttpControlledException(Exception):
    """
    Exception raised for controlled HTTP errors.

    Attributes:
        message (str): Explanation of the error.
        code (int): HTTP status code (default is 400).
    """
    def __init__(self, message: str, code: int = HTTPStatus.BAD_REQUEST):
        self.message = message
        self.code = code
        
        if code not in HTTP_STATUS_CODES.keys():
            raise ValueError("Invalid HTTP status code")
        
        super().__init__(self.message, self.code)