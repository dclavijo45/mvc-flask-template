from database.integrations.db_integration import db
from sqlalchemy.sql import func

class UserModel(db.Model):
    """
    Represents a user in the application.
    
    Attributes:
        id (int): Primary key, unique identifier for the user.
        name (str): The user's name. Must be unique and up to 15 characters.
        age (int): The user's age.
        email (str): The user's email address. Must be unique and up to 255 characters.
        gender (str): The user's gender, represented as a single character.
        created_at (datetime): Timestamp when the user was created.
        updated_at (datetime): Timestamp when the user was last updated.
    Args:
        name (str): The user's name.
        age (int): The user's age.
        email (str): The user's email address.
        gender (str): The user's gender, as a single character.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(15), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    gender = db.Column(db.String(1), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime(),
        server_default=func.now(),
        onupdate=func.current_timestamp(),
        nullable=False,
    )

    def __init__(self, name: str, age: int, email: str, gender: str):
        self.name = name
        self.age = age
        self.email = email
        self.gender = gender
        