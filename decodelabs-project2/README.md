## What I built
In Project 1 - data was stored in a list in memory, whenever server restarts everything is gone. To overcome this problem in Project 2 I solved that problem by connecting the API to a real database so the data is now permanently saved 

Specifically:

A FastAPI server connected to a PostgreSQL database

A User table in the database with fields — id, email, age, is_active, created_at

Duplicate prevention — if same email is submitted twice it returns 409 Conflict.

All responses are in JSON format and the server runs locally on port 8000.

## Technologies Used
Python 

FastAPI 

SQLAlchemy 

PostgreSQL 

Pydantic 

psycopg2 

Uvicorn 

python-dotenv 

pgAdmin 

## How to run this project
It runs locally on your computer meaning only you can access it right now.
When you ran:
```
uvicorn main:app --reload
```

```
http://127.0.0.1:8000/docs
```

---

## API Routes
POST /users → creates a new user and saves permanently to database

GET /users → reads all users from database

GET /users/{id} → reads a single user by id

PUT /users/{id} → updates an existing user,

DELETE /users/{id} → deletes a user

## What I learned
In this project I learned how to connect the API with a real database. Data Persistence - difference between volatile memory (list) and permanent storage (database). HTTP 409 Conflict - new status code for handling duplicate entries. UserCreate vs UserResponse - why input and output models should be separate for security
