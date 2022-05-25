from typing import Dict
from sqlalchemy.orm import Session
import schemas, models


def get_users(db:Session):
    users = db.query(models.User).all()
    return users
    # print(users[0].id)

def get_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user
    print(user, '==================')

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db:Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # print(db_user, 'ccccccccccccc')
    return db_user


def update_user(db: Session, id: int, email: str, is_active: bool):
    user_to_update = get_user(db=db, id=id)
    user_to_update.email = email
    user_to_update.is_active = is_active
    db.commit()
    db.refresh(user_to_update)
    return user_to_update

def delete_user(db:Session, id: int):
    user = get_user(db=db, id=id)
    db.delete(user)
    db.commit()
    return user