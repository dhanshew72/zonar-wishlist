"""
Handles routing for all API traffic
"""
from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from app.models.book import Book, BookKey, BookUpdate
from app.models.login import Login
from app.services.auth import Auth
from app.services.wishlist import Wishlist


router = APIRouter()


def validate_login(login):
    """
    Validates a login and throws exception if user not found
    """
    result = Auth.check_login(login.email, login.password)
    if not result:
        raise HTTPException(status_code=404, detail="User/password combination not found!")


@router.post("",
             description="Add book to a users wishlist",
             status_code=201)
def add(login: Login, book: Book):
    """
    Handles additions of a single book to a users wishlist
    """
    validate_login(login)
    result = Wishlist(login.email).add(jsonable_encoder(book))
    if not result['is_successful']:
        raise HTTPException(status_code=result['code'], detail=result['msg'])
    return result['msg']


@router.get("",
            description="Read a users wishlist",
            status_code=200)
def read(login: Login = Depends()):
    """
    Retrieves an entire users wishlist
    """
    validate_login(login)
    return Wishlist(login.email).read()


@router.put("",
            description="Update a book in a users wishlist",
            status_code=200)
def update(login: Login, book_update: BookUpdate):
    """
    Handles update of a single book to a users wishlist
    """
    validate_login(login)
    result = Wishlist(login.email).update(jsonable_encoder(book_update))
    if not result['is_successful']:
        raise HTTPException(status_code=result['code'], detail=result['msg'])
    return result['msg']


@router.delete("",
               description="Remove a book from a users wishlist",
               status_code=200)
def remove(login: Login, book_key: BookKey):
    """
    Remove a book from a users wishlist
    """
    validate_login(login)
    result = Wishlist(login.email).remove(book_key.isbn)
    if not result['is_successful']:
        raise HTTPException(status_code=result['code'], detail=result['msg'])
    return result['msg']
