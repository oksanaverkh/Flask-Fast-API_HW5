# Задание №7
# Создать RESTful API для управления списком задач.
# Приложение должно использовать FastAPI и поддерживать следующие функции:
# ○ Получение списка всех задач.
# ○ Получение информации о задаче по её ID.
# ○ Добавление новой задачи.
# ○ Обновление информации о задаче по её ID.
# ○ Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля: ID (целое число),
# Название (строка), Описание (строка), Статус (строка): "todo", "in progress","done".
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте функцию get_tasks для получения списка всех задач (метод GET).
# Создайте функцию get_task для получения информации о задаче по её ID (метод GET).
# Создайте функцию create_task для добавления новой задачи (метод POST).
# Создайте функцию update_task для обновления информации о задаче по её ID (метод PUT).
# Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).

from .pydantic_models import Task
from fastapi import FastAPI

app = FastAPI()
tasks: list[Task] = []


@app.get('/')
async def get_tasks():
    return tasks


@app.post('/tasks/{task_id}')
async def get_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    return filtered_tasks



@app.post('/tasks/')
async def create_task(task: Task):
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, new_task: Task):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'updated': False}
    task = filtered_tasks[0]

    task.title = new_task.title
    task.description = new_task.description
    if new_task.status in ['todo', 'in progress', 'done']:
        task.status = new_task.status
    else:
        task.status = 'todo'
    return {'updated': True, 'task': new_task}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'deleted': False}
    task = filtered_tasks[0]

    tasks.remove(task)
    return {'deleted': True}
