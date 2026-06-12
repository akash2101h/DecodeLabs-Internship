## What I built
A secure authentication system using FastAPI,
Users can register with email, password and age,
Password is never stored as plain text it gets hashed using bcrypt,
After login server returns a JWT token,
Protected routes can only be accessed with a valid token,
Token expires after 30 minutes.

Specifically:
A FastAPI server connected to a PostgreSQL database
A User table in the database with fields — id, email, age, passwrod, is_active, created_at
Duplicate prevention - if same email is submitted twice it returns 409 Conflict.
401 Unauthorized - when token is missing or invalid

All responses are in JSON format and the server runs locally on port 8000.

## Technologies Used
Python 
FastAPI 
SQLAlchemy 
PostgreSQL 
Pydantic 
Passlib + bcrypt 
python-jose 
Uvicorn 
python-dotenv
Postman 

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
POST /register — creates a new user account with hashed password, returns 201
POST /login — verifies email and password, returns JWT token
GET /users — returns all users without password field, returns 200
GET /users/{user_id} — returns single user by ID without password, returns 200
GET /users/me — returns only your own profile, returns 200

## What I learned
Before this project I had no idea how authentication works. I learned that passwords should never be stored as plain text 
and bcrypt is used to hash them. I also learned about JWT tokens and how they are used to protect routes instead of sending 
password every time. The concept of role based access control was new to me where server controls the role not the user.