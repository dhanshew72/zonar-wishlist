"""
Handles the CRUD (minus the R) operations for a wishlist bby interacting with the FAKE_DB

The code is a bit ugly using the FAKE_DB, ideally we'd use SQLAlchemy with an ORM, but I didn't
get the time to use this.
"""
from app.db import FAKE_DB


class Wishlist:

    def __init__(self, email):
        """
        Initializes a users wishlist (utilizes FAKE_DB)
        """
        self.email = email

    def add(self, book):
        """
        Add a single book to a users wishlist
        """
        if FAKE_DB[self.email]['wishlist'].get(book['isbn']):
            return {'is_successful': False, 'msg': 'Book already exists in wishlist', 'code': 400}
        FAKE_DB[self.email]['wishlist'][book['isbn']] = book
        return {'is_successful': True, 'msg': 'Book successfully added to wishlist'}

    def update(self, book_updates):
        """
        Update a single book in a users wishlist

        Note: Updating the ISBN is a bit hacky with the fake DB setup, but in a database we'd just update
        the unique value and change it once instead of two places, otherwise I am forcing the user to remove/add with
        new isbn for now.
        """
        if book_updates['attribute'] == 'isbn':
            return {'is_successful': False, 'msg': 'Cannot update ISBN, please remove/re-add book', 'code': 400}
        if not FAKE_DB[self.email]['wishlist'].get(book_updates['isbn']):
            return {'is_successful': False, 'msg': 'Book not found in wishlist', 'code': 404}
        if not FAKE_DB[self.email]['wishlist'][book_updates['isbn']].get(book_updates['attribute']):
            return {'is_successful': False, 'msg': 'Not a valid attribute of a book!', 'code': 400}
        FAKE_DB[self.email]['wishlist'][book_updates['isbn']][book_updates['attribute']] = book_updates['value']
        return {'is_successful': True, 'msg': 'Book updated successfully'}

    def read(self):
        """
        Retrieves an entire users wishlist
        """
        return FAKE_DB[self.email]['wishlist']

    def remove(self, isbn):
        """
        Removes a single book from a users wishlist
        """
        if not FAKE_DB[self.email]['wishlist'].get(isbn):
            return {'is_successful': False, 'msg': 'Book not found in wishlist', 'code': 404}
        del FAKE_DB[self.email]['wishlist'][isbn]
        return {'is_successful': True, 'msg': 'Book successfully removed'}
