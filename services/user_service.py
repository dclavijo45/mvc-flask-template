from exceptions.controlled_exception import HttpControlledException
from database.repository.user_repository import UserRepository
from database.schemas.user_schema import UserSchema
from marshmallow.exceptions import ValidationError
from database.models.user_model import UserModel
from types_dict.http import HttpGlobalResponse
from http import HTTPStatus
from flask import jsonify
from typing import Any

class UserService:
    """
    Service class for managing user-related operations.
    
    Methods:
        __init__():
            Initializes the UserService with a user repository and schema.
        get_users():
            Retrieves all users from the repository.
        create_user(user: dict[str, Any]):
            Creates a new user from the provided dictionary. Validates input, checks for duplicate emails,
            and returns a success message or raises an exception on error.
    """
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_schema = UserSchema()

    def get_users(self):
        users = self.user_repository.get_users()
        return jsonify(self.user_schema.dump(users, many=True))

    def create_user(self, user: dict[str, Any]):
        try:
            user_data: dict[str, Any] = self.user_schema.load(user) # type: ignore
        
            if self.user_repository.get_user_by_email(user_data["email"]):
                raise HttpControlledException("User with this email already exists", HTTPStatus.CONFLICT)
            
            self.user_repository.create_user(UserModel(**user_data))
            
            response: HttpGlobalResponse = {
                "message": "User created successfully",
            }
            
            return jsonify(response), HTTPStatus.CREATED
        except ValidationError as validation_error:
            message_error = ""
            
            for key in validation_error.messages.keys(): # type: ignore
                for error in validation_error.messages[key]: # type: ignore
                    message_error += f"{key}: {error} "
            
            message_error = message_error.strip()
            raise HttpControlledException(message_error)