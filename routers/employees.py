from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from ..schemas.employee_schema import EmployeeCreate, Employee, EmployeeUpdate
from ..utils.storage import Storage
from ..auth import get_token_header

router = APIRouter()
storage = Storage()

@router.post("/", response_model=Employee, status_code=status.HTTP_201_CREATED,
             summary="Create an employee", description="Create a new employee record.")
async def create_employee(employee: EmployeeCreate, token: str = Depends(get_token_header)):
    emp = storage.create_employee(employee)
    return emp

@router.get("/", response_model=List[Employee], summary="List employees")
async def list_employees():
    return storage.list_employees()

@router.get("/{employee_id}", response_model=Employee, summary="Get employee details")
async def get_employee(employee_id: int):
    emp = storage.get_employee(employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{employee_id}", response_model=Employee, summary="Update employee")
async def update_employee(employee_id: int, payload: EmployeeUpdate, token: str = Depends(get_token_header)):
    emp = storage.update_employee(employee_id, payload)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete employee")
async def delete_employee(employee_id: int, token: str = Depends(get_token_header)):
    ok = storage.delete_employee(employee_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Employee not found")
    return None
