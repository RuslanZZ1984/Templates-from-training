from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return FileResponse("E:\Обучение Python\FastAPI\Практика\indexx.html")

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )