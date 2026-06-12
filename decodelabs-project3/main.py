from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, get_db
from auth import verify_password, create_access_token, verify_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = crud.get_user_by_email(db, payload.get("sub"))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.post("/register", status_code=201, response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")
    return crud.create_user(db, user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.UserResponse)
def get_my_profile(current_user = Depends(get_current_user)):
    return current_user

@app.get("/users", status_code=200, response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_users(db)

@app.get("/users/{user_id}", status_code=200, response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user