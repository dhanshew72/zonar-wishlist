"""
Checks FAKE_DB for matching email and password
"""
from app.db import FAKE_DB


class Auth:

    @staticmethod
    def check_login(email, password):
        """
        Checks if a  login is valid
        """
        if FAKE_DB[email]:
            if FAKE_DB[email]['password'] == password:
                return True
        return False
