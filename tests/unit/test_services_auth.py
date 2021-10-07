import unittest

from app.services.auth import Auth


class TestService(unittest.TestCase):

    def test_check_login(self):
        tests = [
            {
                'email': 'alice@example.com',
                'password': 'secret',
                'expected': True
            },
            {
                'email': 'alice@example.com',
                'password': 'wrongpass',
                'expected': False
            }
        ]
        for test in tests:
            result = Auth.check_login(test['email'], test['password'])
            self.assertEqual(test['expected'], result)
