from fastapi import FastAPI
from database import engine, Base
import models, api

app = FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(api.router, prefix="/todo", tags=[])