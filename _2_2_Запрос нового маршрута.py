from fastapi import FastAPI
import uvicorn

app = FastAPI()


# пример роута (маршрута): Запускается как http://localhost:8000
@app.get("/")
def read_root():
    return {"message": "Hello, World"}


# новый роут: Запускается как http://localhost:8000/custom
@app.get("/custom")
def read_custom_message():
    return {'message': 'This is a custom message'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
