import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from models.models import User

app = FastAPI()

# Пример пользовательских данных (для демонстрационных целей)
fake_users = {
    1: {'username': "john_doe", 'email': "john@example.com"},
    2: {'username': "jane_smith", 'email': 'jane@example.com'}
}

# Конечная точка для получения информации о пользователе по ID
@app.get('/users/{user_id}')
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {'error': 'User not found'}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )