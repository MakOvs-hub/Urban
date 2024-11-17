from fastapi import FastAPI

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
async def user_page(user_id):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user") # передача данных будет осуществляться в адресной строке
async def user_str_page(username, age):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
