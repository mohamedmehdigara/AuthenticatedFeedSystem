from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import User, Gender, Role
app = FastAPI()

db: List[User] = [
    User(id=uuid4(), first_name="Jamila",
         last_name="Ahmed", gender=Gender.female, roles=[Role.Student]),
    User(id=uuid4(), first_name="Alex",
         last_name="Clover", gender=Gender.female, roles=[Role.admin, Role.User])
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db
