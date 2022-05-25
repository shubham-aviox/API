from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router: APIRouter = APIRouter()

@router.post("/todo", status_code=status.HTTP_201_CREATED)
def create(todo: schemas.ToDoRequest, db: Session=Depends(get_db)):
	todo = crud.create_todo(db, todo=todo.task)
	return todo


@router.get("/todo/{id}", status_code=status.HTTP_201_CREATED)
def read(id, db: Session=Depends(get_db)):
	todo = crud.read_todo(db, id=id)
	return todo


@router.put("/todo/{id}", status_code=status.HTTP_201_CREATED)
def update(id, task, db: Session=Depends(get_db)):
	todo = crud.update_todo(db,task=task, id=id)
	return todo