# Flask API - My First Flask API with SQLAlchemy

This is my first Flask API, built as a simple user creation service with SQLAlchemy as the ORM. It includes basic authentication, user creation, and database interaction. The project also demonstrates the use of decorators for logging and managing routes.

## Features

- **User Creation**: POST endpoint to create a new user with hashed passwords.
- **SQLAlchemy ORM**: Interacts with a PostgreSQL database using SQLAlchemy for data modeling and query management.
- **Decorators**: Custom decorators to log data and apply necessary middleware functions.
- **JWT Authentication**: Token-based authentication for securing user routes (yet to be implemented fully).
  
## Dependencies

This project requires the following Python packages:

- `Flask`: The web framework used to build the API.
- `Flask-SQLAlchemy`: SQLAlchemy integration with Flask for ORM-based database management.
- `Flask-Migrate`: For database migrations (optional but useful for production).
- `python-dotenv`: To manage environment variables securely.
- `Werkzeug`: Used for hashing passwords securely.
- `psycopg2`: PostgreSQL adapter for Python.
- `Flask-Blueprints`: To structure the API in a modular way using Blueprints.
  
### Install Dependencies

To install the dependencies, use the following command:

```bash
pip install -r requirements.txt