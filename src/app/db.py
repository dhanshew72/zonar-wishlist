"""
This is a mock DB using a local variable instead of an actual database
"""
FAKE_DB = {
    "alice@example.com": {
        "first_name": "Alice",
        "last_name": "Wonder",
        "email": "alice@example.com",
        "password": "secret",
        "wishlist": {
            "9783161484100": {
                "title": "My Book",
                "author": "The Author",
                "isbn": "9783161484100",
                "date_of_publication": "2020-03-15"
            }
        }
    }
}
