from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool

class Feedback(BaseModel):
    name: str
    message: str

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    tags: list
