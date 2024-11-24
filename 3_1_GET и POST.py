import uvicorn

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from models.models import UserCreate, Feedback, Item

app = FastAPI()
users: list = []


@app.post("/create_user/")
async def create_user(new_user: UserCreate):
    users.append(new_user)
    return new_user

@app.get('/showuser')
async def show_user():
    return {'users': users}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
