import unittest

from app.services.wishlist import Wishlist


class TestServiceWishlist(unittest.TestCase):

    def test_add(self):
        tests = [
            {
                'email': 'alice@example.com',
                'book': {
                    'isbn': '9783161484100',
                    'title': 'My book',
                    'author': 'The Author',
                    'date_of_publication': '2020-03-07',
                },
                'expected': {'code': 400, 'is_successful': False, 'msg': 'Book already exists in wishlist'}
            },
            {
                'email': 'alice@example.com',
                'book': {
                    'isbn': '9783161484101',
                    'title': 'My book',
                    'author': 'The Author',
                    'date_of_publication': '2020-03-07',
                },
                'expected': {'is_successful': True, 'msg': 'Book successfully added to wishlist'}
            }
        ]
        for test in tests:
            result = Wishlist(test['email']).add(test['book'])
            self.assertEqual(test['expected'], result)

    def test_update(self):
        tests = [
            {
                'email': 'alice@example.com',
                'updates': {
                    'isbn': '9783161484101',
                    'attribute': 'title',
                    'value': 'my book 3',
                },
                'expected': {'is_successful': True, 'msg': 'Book updated successfully'}
            },
            {
                'email': 'alice@example.com',
                'updates': {
                    'isbn': '9783161484101',
                    'attribute': 'isbn',
                    'value': '9783161484102',
                },
                'expected': {'is_successful': False, 'msg': 'Cannot update ISBN, please remove/re-add book', 'code': 400}
            }
        ]
        for test in tests:
            result = Wishlist(test['email']).update(test['updates'])
            self.assertEqual(test['expected'], result)

    def test_remove(self):
        tests = [
            {
                'email': 'alice@example.com',
                'isbn': '9783161484100',
                'expected': {'is_successful': True, 'msg': 'Book successfully removed'}
            },
            {
                'email': 'alice@example.com',
                'isbn': 'nonexistent',
                'expected': {'is_successful': False, 'msg': 'Book not found in wishlist', 'code': 404}
            }
        ]
        for test in tests:
            result = Wishlist(test['email']).remove(test['isbn'])
            self.assertEqual(test['expected'], result)
