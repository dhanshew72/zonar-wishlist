import requests


class TestWishlist:

    def test_wishlist(self):
        """
        Must run a docker container before running this module!
        """
        url = 'http://localhost:8080/wishlist'
        tests = [
            {
                'request_type': 'POST',
                'body': {
                    'json': {
                        'login': {
                            'email': 'alice@example.com',
                            'password': 'secret'
                        },
                        'book': {
                            'title': 'New book',
                            'author': 'John',
                            'isbn': '9783161484103',
                            "date_of_publication": "2020-03-16"
                        }
                    }
                },
                'expected': 'Book successfully added to wishlist'
            },
            {
                'request_type': 'POST',
                'body': {
                    'json': {
                        'login': {
                            'email': 'alice@example.com',
                            'password': 'secret'
                        },
                        'book': {
                            'title': 'New book',
                            'author': 'John',
                            'isbn': '9783161484103',
                            "date_of_publication": "2020-03-16"
                        }
                    }
                },
                'expected': {'detail': 'Book already exists in wishlist'}
            },
            {
                'request_type': 'PUT',
                'body': {
                    'json': {
                        'login': {
                            'email': 'alice@example.com',
                            'password': 'secret'
                        },
                        'book_update': {
                            'attribute': 'title',
                            'value': 'My updated book',
                            'isbn': '9783161484103'
                        }
                    }
                },
                'expected': 'Book updated successfully'
            },
            {
                'request_type': 'DELETE',
                'body': {
                    'json': {
                        'login': {
                            'email': 'alice@example.com',
                            'password': 'secret'
                        },
                        "book_key": {
                            "isbn": "9783161484103"
                        }
                    }
                },
                'expected': 'Book successfully removed'
            },
            {
                'request_type': 'DELETE',
                'body': {
                    'json': {
                        'login': {
                            'email': 'alice@example.com',
                            'password': 'secret'
                        },
                        "book_key": {
                            "isbn": "9783161484103"
                        }
                    }
                },
                'expected': {'detail': 'Book not found in wishlist'}
            }
        ]
        for test in tests:
            res = requests.request(test['request_type'], url, **test['body']).json()
            assert res == test['expected']
        print('Functional test passed!')


if __name__ == '__main__':
    TestWishlist().test_wishlist()
