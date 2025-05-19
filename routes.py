from controllers.user_controller import UserController
from types_dict.routes import Routes

routes: list[Routes] = [
    {
        "rule_path": "/user",
        "controller": UserController.as_view("user"),
    }
]
