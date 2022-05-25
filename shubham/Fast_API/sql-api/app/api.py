from sqlalchemy.orm import Session
from models import User
import crud
import schemas
from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db

router: APIRouter = APIRouter()

@router.get('/user/', response_model=list[schemas.User])
def get_user_by_id(db: Session=Depends(get_db)):
    user = crud.get_users(db=db)
    return user
    # print(user, 'ggggggggggggggg')

@router.get('/user/{email}/', response_model=schemas.User)
def get_user_by_email(email: str, db: Session=Depends(get_db)):
    user = crud.get_user_by_email(db=db, email=email)
    return user

@router.get('/user/{id}', response_model=schemas.User)
def get_user_by_id(id: int, db: Session=Depends(get_db)):
    user = crud.get_user(db=db, id=id)
    print(user, 'ggggggggggggggg')
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user


@router.post('/create/user', response_model=schemas.User)
def create(user: schemas.UserCreate, db: Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    print(db_user, 'uuuuuuuuuuuuu')
    return crud.create_user(db=db, user=user)
    

@router.put('/update/{id}', response_model=schemas.User)
def update(id: int, email: str, is_active: bool, db: Session=Depends(get_db)):
    user = crud.update_user(db=db, id=id,  email=email, is_active=is_active)
    return user


@router.delete('/user/delete/{id}/', response_model=schemas.User)
def user_delete(id: int,  db: Session=Depends(get_db)):
    user = crud.delete_user(db=db, id=id)
    return HTTPException(status_code=404, detail="User not found")