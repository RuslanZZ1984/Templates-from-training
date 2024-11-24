import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from models.models import User

app = FastAPI()
# user = User(name='John Doe', age=25)

# @app.get('/users', response_model=User)
# def user_root():
#     return user

@app.post('/add_user')
async def add_user(user: User):
    if user.age >=18:
        user.is_adult = True
    return user

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )
