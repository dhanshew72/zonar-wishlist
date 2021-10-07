"""
Models for all books and operations
"""
from pydantic import BaseModel, Field
from datetime import date


class BookKey(BaseModel):
    """
    Model for key of a book
    """
    # isbn's are unique and have 13 characters
    isbn: str = Field(min_length=12)


class Book(BookKey):
    """
    Model for all book attributes
    """
    title: str
    author: str
    date_of_publication: date


class BookUpdate(BookKey):
    """
    Model for updating a book
    """
    attribute: str
    value: str
