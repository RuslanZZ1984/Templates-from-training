# import uvicorn

from datetime import date

from pydantic import BaseModel


# Объявляем параметр user_id с типом 'str'
# и получаем поддержку проверки типов данных редактора (IDE) внутри функции
def main(user_id: str):
    return user_id


# Модель Pydantic - ещё один пример создания
class User(BaseModel):
    id: int
    name: str
    joined: date


my_user: User = User(id=3, name='John Doe', joined='2018-07-19')

second_user_data = {
    'id': 4,
    'name': "Mary",
    'joined': '2018-11-30',
}

my_second_user: User = User(**second_user_data)

print(my_user)
print(my_second_user)

# if __name__ == '__main__':
#     uvicorn.run(
#         'main:app',
#         host = '127.0.0.1',
#         port = 8000,
#         reload = True
#     )
