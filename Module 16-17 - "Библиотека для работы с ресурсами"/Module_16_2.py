'''
Допишите валидацию для маршрутов из предыдущей задачи при помощи классов Path и Annotated:
'/user/{user_id}' - функция, выполняемая по этому маршруту, принимает аргумент user_id, для которого необходимо написать следующую валидацию:
Должно быть целым числом
Ограничено по значению: больше или равно 1 и меньше либо равно 100.
Описание - 'Enter User ID'
Пример - '1' (можете подставить свой пример не противоречащий валидации)
'/user' замените на '/user/{username}/{age}' - функция, выполняемая по этому маршруту, принимает аргументы username и age,
для которых необходимо написать следующую валидацию:
username - строка, age - целое число.
username ограничение по длине: больше или равно 5 и меньше либо равно 20.
age ограничение по значению: больше или равно 18 и меньше либо равно 120.
Описания для username и age - 'Enter username' и 'Enter age' соответственно.
Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации).
'''
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
#json - javascript object notation

@app.get("/")# ручка/endpoint с помощью нее мы можем переходить
                # по значениям (адрес в браузере) ..../docs
async def main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description = 'Enter User ID', example= '13')]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}") # передача данных будет осуществляться в адресной строке
async def user_str_page(username: str = Path(min_length=5, max_length=20, description = 'Enter username', example= 'UrbanUser'),
                        age: int = Path(ge=18, le=120, description = 'Enter age', example= '24')):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}