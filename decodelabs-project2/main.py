from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

# this creates the tables in PostgreSQL automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# GET all users
@app.get("/users", status_code=200)
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# GET single user
@app.get("/users/{user_id}", status_code=200)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST create user
@app.post("/users", status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check for duplicate email
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")
    return crud.create_user(db, user)

# PUT update user
@app.put("/users/{user_id}", status_code=200)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

# DELETE user
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")