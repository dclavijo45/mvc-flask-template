from services.user_service import UserService
from flask.views import MethodView
from flask import request

class UserController(MethodView):
    """
    UserController handles HTTP requests related to user operations.
    
    Methods:
        post():
            Handles POST requests to create a new user.
            Expects JSON data in the request body.
            Returns the result of the user creation process.
        get():
            Handles GET requests to retrieve a list of users.
            Returns a list of users.
    """
    def post(self):
        user_service = UserService()
        return user_service.create_user(request.get_json());
    
    def get(self):
        user_service = UserService()
        return user_service.get_users()