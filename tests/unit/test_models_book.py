import unittest

from app.models.book import Book


class TestModelBook(unittest.TestCase):

    def test_book(self):
        tests = [
            {
                'title': 'My Book',
                'author': 'My author',
                'date_of_publication': '2020-03-15',
                'isbn': '1234567890123',
                'expected': Book(
                    isbn='1234567890123',
                    title='My Book',
                    author='My author',
                    date_of_publication='2020-03-15'
                )
            }
        ]
        for test in tests:
            result = Book(**test)
            self.assertEqual(test['expected'], result)
