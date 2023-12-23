# Задание №8
# Необходимо создать API для управления списком задач. Каждая задача должна
# содержать заголовок и описание. Для каждой задачи должна быть возможность
# указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# ○ GET /tasks - возвращает список всех задач.
# ○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.
# ○ POST /tasks - добавляет новую задачу.
# ○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.
# ○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. 
# Для этого использовать библиотеку Pydantic

from .pydantic_models import Task2
from fastapi import FastAPI

app = FastAPI()
tasks: list[Task2] = []


@app.get('/')
async def get_tasks():
    return tasks


@app.post('/tasks/{task_id}')
async def get_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    return filtered_tasks



@app.post('/tasks/')
async def create_task(task: Task2):
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, new_task: Task2):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'updated': False}
    task = filtered_tasks[0]

    task.title = new_task.title
    task.description = new_task.description
    
    if new_task.status in ['выполнена', 'не выполнена']:
        task.status = new_task.status
    else:
        task.status = 'не выполнена'
    return {'updated': True, 'task': new_task}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    if not filtered_tasks:
        return {'deleted': False}
    task = filtered_tasks[0]

    tasks.remove(task)
    return {'deleted': True}