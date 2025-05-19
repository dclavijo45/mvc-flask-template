from flask.typing import RouteCallable
from typing import TypedDict

class Routes(TypedDict):
    """
    Routes is a TypedDict that defines the structure for route configurations.

    Attributes:
        rule_path (str): The path for the route.
        controller (object): The controller associated with the route.
    """
    rule_path: str
    controller: RouteCallable