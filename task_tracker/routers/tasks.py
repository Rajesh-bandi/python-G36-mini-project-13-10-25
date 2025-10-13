from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from ..schemas.task_schema import TaskCreate, Task, TaskUpdate, TaskStatus
from ..utils.storage import Storage
from ..auth import get_token_header

router = APIRouter()
storage = Storage()

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED, summary="Create task")
async def create_task(task: TaskCreate, token: str = Depends(get_token_header)):
    t = storage.create_task(task)
    return t

@router.get("/", response_model=List[Task], summary="List tasks")
async def list_tasks(status: Optional[TaskStatus] = None, assigned_to: Optional[int] = None):
    return storage.list_tasks(status=status, assigned_to=assigned_to)

@router.get("/{task_id}", response_model=Task, summary="Get task")
async def get_task(task_id: int):
    t = storage.get_task(task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return t

@router.put("/{task_id}", response_model=Task, summary="Update task")
async def update_task(task_id: int, payload: TaskUpdate, token: str = Depends(get_token_header)):
    t = storage.update_task(task_id, payload)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return t

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete task")
async def delete_task(task_id: int, token: str = Depends(get_token_header)):
    ok = storage.delete_task(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
