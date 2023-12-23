from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str = 'todo'

class Task2(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str = 'не выполнена'

