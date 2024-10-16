from fastapi import FastAPI
from my_project import crud, models, schemas
from my_project.database import engine
from sqlalchemy.orm import Session

app = FastAPI()

# Sample FastAPI route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Business API"}

# Add your API routes here using FastAPI, for example:
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    with Session(engine) as session:
        items = crud.get_items(session, skip=skip, limit=limit)
    return items
