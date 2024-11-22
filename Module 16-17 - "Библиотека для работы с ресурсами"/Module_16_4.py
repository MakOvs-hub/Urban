'''
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
'''


from fastapi import FastAPI, Path, HTTPException, Body
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int # номер пользователя
    username: str # имя пользователя
    age: int # возраст пользователя

@app.get("/")
def get_all_messages() -> List[User]:
    return users

@app.get('/users')
def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
def create_user(user: User, username: str, age: int) -> str: # обязательно присвой объект классу
    user.id = (len(users)+ 1)
    user.username = username
    user.age = age
    users.append(user)
    return f"User created."

@app.put('/user/{user_id}/{username}/{age}')
def edit_user(user_id:int , username:str, age:int ) -> str:
    try:
        edit_us = users[user_id - 1]
        edit_us.age = age
        edit_us.username = username
        return f"User update."
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
def del_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User {user_id} was deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
