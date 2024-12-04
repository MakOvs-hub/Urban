from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session # Сессия БД
from app.backend.db_depends import get_db # Функция подключения к БД
from typing import Annotated # Аннотации, Модели БД и Pydantic.
from app.Models import Task, User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete # Функции работы с записями.
from slugify import slugify # Функция создания slug-строки

router = APIRouter(prefix= '/task',tags=['task'])

@router.get ('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    '''
    Функция all_tasks ('/') - идентично all_users.
    '''
    tasks = db.scalars(select(Task)).all()
    if tasks is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no users')
    return tasks

@router.get ('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    '''
    Функция task_by_id ('/task_id') - идентично user_by_id (тоже по id)выбрасывает исключение с кодом 404 и описанием "User was not found"
    '''
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return task

@router.post ('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    '''
    Функция craete_task ('/create'):
Дополнительно принимает модель CreateTask и user_id.
Подставляет в таблицу Task запись значениями указанными в CreateUser и user_id, если пользователь найден.
    Т.е. при создании записи Task вам необходимо связать её с конкретным пользователем User.
В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
В случае отсутствия пользователя выбрасывает исключение с кодом 404 и описанием "User was not found"
    '''
    task_by_user = db.scalar(select(User).where(User.id == user_id))
    if task_by_user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    db.execute(insert(Task).values(title = create_task.title,
                                   content = create_task.content,
                                   priority=create_task.priority,
                                   user_id = task_by_user.id,
                                   slug = slugify(create_task.title)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put ('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, task_id: int):
    '''
    Функция update_task ('/update') - идентично update_user.
    '''
    task_update = db.scalar(select(Task).where(Task.id == task_id))
    if task_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

    db.execute(update(User).where(Task.id == task_id).values(title=update_task.title,
                                                             content=update_task.content,
                                                             priority=update_task.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK,'transaction': 'Task update is successful!'}

@router.delete ('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    '''
   Функция delete_task ('/delete') - идентично delete_user.
    '''
    task_delete = db.scalar(select(Task).where(Task.id == task_id))
    if task_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task was deleted.'}
