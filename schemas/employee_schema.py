from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class EmployeeBase(BaseModel):
    name: str = Field(..., example="Alice Johnson")
    email: EmailStr = Field(..., example="alice@example.com")
    role: Optional[str] = Field(None, example="Engineer")
    department: Optional[str] = Field(None, example="R&D")


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    department: Optional[str]


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
