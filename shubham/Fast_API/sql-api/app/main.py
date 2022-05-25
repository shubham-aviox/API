from fastapi import FastAPI, Header, HTTPException
from database import get_db, engine
import crud, models, api

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(api.router, prefix="/app", tags=[])