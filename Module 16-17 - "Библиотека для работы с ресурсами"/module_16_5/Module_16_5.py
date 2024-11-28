'''

Измените и дополните ранее описанные CRUD запросы:
Напишите новый запрос по маршруту '/':
Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и список users.
Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.

Измените get запрос по маршруту '/user' на '/user/{user_id}':
Функция по этому запросу теперь принимает аргумент request и user_id.
Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html',
а также передавать в него request и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
'''


from fastapi import FastAPI, Path, HTTPException, Body, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI(swagger_ui_parameters={"tryItOutEnable": True}, debug=True)
templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int # номер пользователя
    username: str # имя пользователя
    age: int # возраст пользователя

@app.get("/")
def get_all_messages(request: Request ) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {'request': request, "users": users})

@app.get('/user/{user_id}')
def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {'request': request, "user": users[user_id]})
    except:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")



@app.post('/user/{username}/{age}')
def create_user(user: User, username: str, age: int) -> str:
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
