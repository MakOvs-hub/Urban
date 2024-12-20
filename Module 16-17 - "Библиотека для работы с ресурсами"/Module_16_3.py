'''
Задача "Имитация работы с БД":
Создайте новое приложение FastAPI и сделайте CRUD запросы.
Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
Реализуйте 4 CRUD запроса:
get запрос по маршруту '/users', который возвращает словарь users.
post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку "User <user_id> is registered".
put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку "The user <user_id> is updated"
delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.
Выполните каждый из этих запросов по порядку.
Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.
'''

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username:str = Path(min_length=5, max_length=20, description = 'Enter username', example= 'UrbanUser'),
                      age:int = Path(ge=18, le=120, description = 'Enter age', example= '18')) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id]= f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered."

@app.put("/user/{user_id}/{username}/{age}")
async def edit_user(user_id:str = Path(min_length=0, max_length=5, description = 'Enter user_id', example= '34'),
                    username:str = Path(min_length=5, max_length=20, description = 'Enter username', example= 'UrbanUser'),
                    age:int = Path(ge=18, le=120, description = 'Enter age', example= '18')) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is updated."

@app.delete("/user/{user_id}")
async def del_user(user_id: Annotated[str, Path(min_length=0, max_length=5, description = 'Enter User ID', example= '13')]) -> str:
    users.pop(user_id)
    return f"User {user_id} was deleted."
