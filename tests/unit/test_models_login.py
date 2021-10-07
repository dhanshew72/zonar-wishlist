import unittest

from app.models.login import Login


class TestModelLogin(unittest.TestCase):

    def test_login(self):
        tests = [
            {
                'email': 'alice@example.com',
                'password': 'my_pass',
                'expected': Login(
                    email='alice@example.com',
                    password='my_pass'
                )
            },
            {
                'email': 'notanemail',
                'password': 'my_pass',
                'has_error': True
            }
        ]
        for test in tests:
            try:
                result = Login(**test)
                self.assertEqual(test['expected'], result)
            except:
                self.assertTrue(test['has_error'])
