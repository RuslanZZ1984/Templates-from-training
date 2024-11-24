import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from models.models import User


app = FastAPI()

fake_db = [{'uernsme': 'vasya', 'user_info': 'любит колбасу'},
           {'username': 'katya', 'user_info': 'любит петь'}]

@app.get('/users')
async def get_all_users():
    return fake_db

@app.post('/add_user') # Маршрут POST для отправления какой-то информации на сервер
async def add_user(user: User): #
    fake_db.append({'username': user.username, 'user_info': user.user_info})
    return {'message': 'юзер успешно добавлен в базу данных'}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )