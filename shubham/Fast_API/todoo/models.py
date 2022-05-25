from database import Base
from sqlalchemy import Integer, String, Column

class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task =  Column(String)