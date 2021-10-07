"""
Model for handling a user login
"""
from pydantic import BaseModel, errors, Field, validator, validate_email


class Login(BaseModel):
    email: str
    password: str = Field(min_length=1)

    @validator("email")
    def check_email(cls, value):
        """
        Validates a single email
        """
        try:
            validate_email(value)
            return value
        except errors.EmailError:
            # Kind of hacky but we want to raise value errors for pydantic instead of email errors
            raise ValueError("Not a valid email: {}".format(value))
