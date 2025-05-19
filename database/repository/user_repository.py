from database.integrations.db_integration import db
from database.models.user_model import UserModel
from typing import Optional

class UserRepository:
    """
    Repository class for managing UserModel database operations.
    
    Methods:
        __init__():
            Initializes the UserRepository instance.
        get_users() -> list[UserModel]:
            Retrieves all users from the database.
        get_user_by_email(email: str) -> Optional[UserModel]:
            Retrieves a user by their email address.
        create_user(user: UserModel):
            Adds a new user to the database and commits the transaction.
            Returns the created user.
    """
    def __init__(self):
        pass
    
    def get_users(self) -> list[UserModel]:
        return UserModel.query.all() # type: ignore
    
    def get_user_by_email(self, email: str) -> Optional[UserModel]:
        return UserModel.query.filter_by(email=email).first() # type: ignore

    def create_user(self, user: UserModel):
        db.session.add(user)
        db.session.commit()
        return user