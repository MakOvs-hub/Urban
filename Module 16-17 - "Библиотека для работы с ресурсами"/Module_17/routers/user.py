from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify # Функция создания slug-строки
from sqlalchemy.orm import Session # Сессия БД
from app.backend.db_depends import get_db # Функция подключения к БД
from typing import Annotated # Аннотации, Модели БД и Pydantic.
from app.Models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete # Функции работы с записями.



router = APIRouter(prefix= '/user',tags=['user'])
'Каждая из нижеперечисленных функций подключается к базе данных в момент обращения при помощи функции get_db - Annotated[Session, Depends(get_db)]'

@router.get ('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    '''
    Функция all_users ('/'):
    Должна возвращать список всех пользователей из БД. Используйте scalars, select и all
    '''
    users = db.scalars(select(User)).all()
    if users is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no users')
    return users

@router.get ('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    '''
    Функция user_by_id ('/user_id'):
Для извлечения записи используйте ранее импортированную функцию select.
Дополнительно принимает user_id.
Выбирает одного пользователя из БД.
Если пользователь не None, то возвращает его.
В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
    :return:
    '''
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return user

@router.post ('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    '''
    Функция craete_user ('/create'):
Для добавления используйте ранее импортированную функцию insert.
Дополнительно принимает модель CreateUser.
Подставляет в таблицу User запись значениями указанными в CreateUser.
В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
Обработку исключения существующего пользователя по user_id или username можете сделать по желанию.
    :return:
    '''
    create_user_dub = db.scalar(select(User).where(User.username == create_user.username))
    if create_user_dub:
        raise HTTPException(status_code=status.HTTP_410_GONE,detail='This username is taken. Try another.')

    db.execute(insert(User).values(username = create_user.username,
                                   firstname = create_user.firstname,
                                   lastname = create_user.lastname,
                                   age = create_user.age,
                                   slug = slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,'transaction': 'Successful'}

@router.put ('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    '''
    Функция update_user ('/update'):
Для обновления используйте ранее импортированную функцию update.
Дополнительно принимает модель UpdateUser и user_id.
Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser. Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
    :return:
    '''
    user_update = db.scalar(select(User).where(User.id == user_id))
    if user_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(update(User).where(User.id == user_id).values(firstname = update_user.firstname,
                                                            lastname = update_user.lastname,
                                                            age = update_user.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK,'transaction': 'User update is successful!'}

@router.delete ('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    '''
    Функция delete_user ('/delete'):
Для удаления используйте ранее импортированную функцию delete.
Всё должно работать аналогично функции update_user, только объект удаляется.
Исключение выбрасывать то же.
    :return:
    '''
    user_delete = db.scalar(select(User).where(User.id == user_id))
    if user_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(delete(Task).where(user_delete.id == Task.user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User was deleted.'}

@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    '''
    Создайте новый маршрут get "/user_id/tasks" и функцию tasks_by_user_id.
    Логика этой функции должна заключатся в возврате всех Task конкретного User по id.
    '''
    tasks_user = db.scalar(select(User).where(User.id == user_id))
    if tasks_user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    task = db.scalars(select(Task).where(tasks_user.id == Task.user_id, Task.completed == False)).all()#execute не сработает
    return task




