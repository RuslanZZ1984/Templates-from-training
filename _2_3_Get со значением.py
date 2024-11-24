import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from models.models import User


app = FastAPI()

@app.get('/{user_id}') # тут объявили параметр пути
async def search_user_by_id(user_id: int): # тут указали его тип данных
    # какая-то логика работы поиска
    return {"вы просили найти юзера с id": user_id}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )