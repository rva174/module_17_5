from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from app.models.task import Task
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


task = APIRouter(prefix="/task", tags=["task"])


################
@task.get("/")
async def all_tasks(db:Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(Task)).all()
    if task is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no tasks'
        )
    return tasks


################
@task.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_value = db.scalar(select(Task).where(Task.id == task_id))
    if task_value is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    return task_value


@task.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask):
    db.execute(insert(Task).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority,
        completed=create_task.completed,
        user_id=update_task.user_id,
        slug=simple_slugify(update_task.title)))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@task.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, update_task: CreateTask):
    task_value = db.scalar(select(Task).where(Task.id == task_id))
    if task_value is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='task was not found'
        )
    db.execute(update(task).where(Task.id == task_id).values(
        title=update_task.title,
        content=update_task.content,
        priority=update_task.priority,
        completed=create_task.completed,
        user_id=update_task.user_id,
        slug=simple_slugify(update_task.title)))


    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@task.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task_value = db.scalar(select(Task).where(Task.id == task_id))
    if task_value is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(delete(User).where(User.task_id == task_id))
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task was deleted successful!'
    }
