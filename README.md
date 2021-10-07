# Wishlist

## Sections

- [Install and Run](#install-and-run)
- [Design & Technology Choices](#design-technology-choices)
- [Next Steps](#next-steps)


<a id="install-and-run"></a>
## Install and Run

This service runs using python3.7. This could cause issues so use the docker
container when possible.

Run the following command to get the virtual environment setup:

```
make dev-env
```

Run the following command to run the service locally outside of docker:

```
make run-local
```

To run unit tests run the following command (ensure virtual environment is not activated):

```
make test
```

To run within a docker container run the following:
```
make run
```
This will build out the container and install dependencies


To run functional tests after setting up the container:
```
make func-test
```

To stop the container run the following:

```
make stop
```

When running the service I just added a fake user: alice@example.com
just to test the service. Each submission requires a login to be submitted
with each request. Here's example requests (you can check /docs endpoint as well):

Add a new book
```
{
  "login": {"email": "alice@example.com", "password": "secret"}
  "book": {"title": "My new book", "author": "The author", "isbn": "9783161484101", "date_of_publication": "2020-03-07"}
}
```

Update a book
```
{
  "login": {
    "email": "alice@example.com",
    "password": "secret"
  },
  "book_update": {
    "isbn": "9783161484101",
    "attribute": "title",
    "value": "My other book"
  }
}
```

Delete a book
```
{
  "login": {
    "email": "alice@example.com",
    "password": "secret"
  },
  "book_key": {
    "isbn": "9783161484101"
  }
}
```

Get a users wishlist
```
<BASE_URL>/wishlist?email=alice@example.com&password=secret
```
Base URL will be localhost:8080 (docker) or 127.0.0.1:8000 (local) depending on how you're running it

<a id="design-technology-choices"></a>
## Design & Technology Choices

Technologies Used:
- FastAPI: Primarily used this to learn more about the framework. I haven't built an
API straight from scratch and wanted to learn how to design it. I also enjoyed using 
the models so that was the basis for using it for this service.
  
- Docker: Easiest way to test running a container instead of ensuring everyone has the same setup as I do.

- PyTest: Using pytest to display results from unit test coverage

Design:

I broke up the roles of each folders under src/app/ like below:

- Routers: Acts as a controller to start when a user communicates with the endpoint
- Models: Handles validation of inputs for the routers. This will run any validation on top as needed
- Services: Handles communication with the "database" and does the CRUD operations
- db.py: The fake database file to handle database connections. Ideally this would setup the connection
and we would have files to map fields to the database to ease updates instead of the hacky code I wrote with a dictionary.
  I've seen schema files mapped it well then we could do lookups.
  
Here's the ideal schema I was thinking:
- users
  - id
  - first_name
  - last_name 
  - email (unique)
  - password
    
- books
  - id
  - title 
  - author 
  - isbn (unique)
  - date_of_publication
    
- wishlist
  - id
  - user_id
  - book_id

The ideal way to handle this is the user_id + book_id is the unique key for wishlist and can
grab all the rows per user_id. Also password would be hashed + salted so only those would be compared
instead of plaintext as I did for now.

<a id="next-steps"></a>
## Next Steps

We have a lot we could do next:
- How we look up books. Right now I only use isbn to lookup but if we had another
unique field or a combination we could search besides having a user update/delete based on ISBN
  
- Add an actual database with the above schema to handle instead of using a fake one

- Add more testing (include integration/actual functional testing). 
  Always could use more tests to handle developer confidence on top of it python has tools like selenium that look intriguing. I need
  more information

- Add more error handling for DB errors and other issues that could occur that's outside of the control of the service

- Login setup is bad, but needs to be broken up. Once a login is successful a user should receive
a token. Once a token retrieved it should be passed in as a header and validated by middleware using dependencies.
  
- The service can be optimized by utilizing async a bit more within the service. As well we can create batch endpoints
to cut down on resource consumption.
  
