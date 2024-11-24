import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from models.models import User, Feedback

app = FastAPI()

# Создаем пустой список, в него будем добавлять данные POST запросов с POSTMAN
lst = []

# POST запрос из POSTMANа
@app.post('/feedback')
async def send_feedback(feedback: Feedback):
    lst.append({'name': feedback.name, 'comments': feedback.message})
    return f'Feedback received. Thank you {feedback.name}!'

# GET запрос
@app.get('/comments')
async def show_feedback():
    return lst

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )