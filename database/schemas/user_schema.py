from marshmallow import Schema, fields, validate
from enums.gender_enum import GenderEnum

class UserSchema(Schema):
    """
    UserSchema defines the serialization and validation rules for User objects.

    Fields:
        id (int): Unique identifier for the user. Read-only.
        name (str): Name of the user. Required. Must be between 1 and 100 characters.
        age (int): Age of the user. Required. Must be between 18 and 120.
        email (str): Email address of the user. Required. Must be a valid email format.
        gender (str): Gender of the user. Required. Must be one of the values defined in GenderEnum.
        created_at (datetime): Timestamp when the user was created. Read-only.
        updated_at (datetime): Timestamp when the user was last updated. Read-only.
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    age = fields.Int(required=True, validate=validate.Range(min=18, max=120))
    email = fields.Email(required=True)
    gender = fields.Str(required=True, validate=validate.OneOf([gender.value for gender in GenderEnum]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)