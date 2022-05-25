import schemas
from sqlalchemy.orm import Session
import models
from fastapi import HTTPException

def create_todo(db: Session, todo: schemas.ToDoRequest):
	todo_db = ToDo(task=todo)
	db.add(todo_db)
	db.commit()
	db.refresh(todo_db)
	return todo_db


def read_todo(db: Session, id: int):
	todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
	if todo:
		print(todo.task)
		return todo
	else:
		raise HTTPException(status_code=404, detail="Not Found")


def update_todo(db: Session, id: int, task: str):
	todo = read_todo(db=db, id=id)
	todo.task = task
	db.commit()
	db.refresh(todo)
	return todo