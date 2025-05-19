from typing import TypedDict

class HttpGlobalResponse(TypedDict):
    """
    A TypedDict representing a global response from an HTTP request.

    Attributes:
        message (str): A message describing the response.
    """
    message: str