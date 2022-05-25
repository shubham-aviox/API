
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     fname = Column(String)
#     lname = Column(String)
#     email = Column(String, unique=True, index=True)
#     todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")


# class TODO(Base):
#     __tablename__ = "todos"
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String, index=True)
#     completed = Column(Boolean, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     owner = relationship("User", back_populates="todos")