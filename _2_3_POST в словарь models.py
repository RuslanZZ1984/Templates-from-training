from pydantic import BaseModel

class User(BaseModel):
    username: str
    user_info: str

class Feedback(BaseModel):
    name: str
    message: str
