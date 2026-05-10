# To-Do List API (Flask + PostgreSQL)

A simple To-Do List API built with Flask, integrated with PostgreSQL, and ready for Railway deployment.

## Features
- CRUD endpoints for To-Do tasks.
- PostgreSQL database integration via Flask-SQLAlchemy.
- Database migrations with Flask-Migrate.
- Ready for Railway deployment.

## Local Setup
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows).
4. Install dependencies: `pip install -r requirements.txt`.
5. Create a `.env` file from `.env.example` and fill in your database details.
6. Run migrations: `flask db init`, `flask db migrate`, `flask db upgrade`.
7. Run the app: `flask run`.

## API Endpoints
- `GET /`: API Info
- `GET /health`: Health Check
- `GET /todos`: List all tasks
- `POST /todos`: Create a new task
- `GET /todos/<id>`: Get a task by ID
- `PUT /todos/<id>`: Update a task
- `DELETE /todos/<id>`: Delete a task
