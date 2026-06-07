from sqlalchemy.orm import Session
import models, schemas

# READ - get all users
def get_users(db: Session):
    return db.query(models.User).all()

# READ - get single user
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# READ - get user by email (for duplicate check)
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# UPDATE
def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.email = user.email
        db_user.age = user.age
        db.commit()
        db.refresh(db_user)
    return db_user

# DELETE
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user