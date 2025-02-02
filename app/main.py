# from app.backend.db import Base
# from fastapi import FastAPI
# from app.routers.user import user
# from app.routers.task import task
# from sqlalchemy import create_engine

# -*- coding: utf-8 -*-
from fastapi import FastAPI
from app.routers.user import user
from app.routers.task import task




# import logging
#python - m
# logging.getLogger("uvicorn").handlers.clear()


app = FastAPI()

# Создание таблиц
# Base.metadata.create_all(bind=create_engine)



@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user)
app.include_router(task)

#from sqlalchemy.schema import CreateTable
#print(CreateTable(Task.__table__))

# if __name__=="__main__":
#     import uvicorn
#     uvicorn.run(app,host='0.0.0.0', port=8000)

# pip install alembic   # установка alembic
# alembic init app/migrations    # создание начальных файлоф
# alembic revision --autogenerate -m "Initial migration"    #После настройки alembic и env
# alembic upgrade head