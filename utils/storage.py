from typing import Dict, List, Optional
from ..schemas.employee_schema import EmployeeCreate, Employee, EmployeeUpdate
from ..schemas.task_schema import TaskCreate, Task, TaskUpdate, TaskStatus


class Storage:
    def __init__(self):
        self._employees: Dict[int, dict] = {}
        self._tasks: Dict[int, dict] = {}
        self._next_employee_id = 1
        self._next_task_id = 1

    # Employee operations
    def create_employee(self, payload: EmployeeCreate) -> Employee:
        emp = payload.dict()
        emp_id = self._next_employee_id
        emp["id"] = emp_id
        self._employees[emp_id] = emp
        self._next_employee_id += 1
        return Employee(**emp)

    def list_employees(self) -> List[Employee]:
        return [Employee(**e) for e in self._employees.values()]

    def get_employee(self, employee_id: int) -> Optional[Employee]:
        e = self._employees.get(employee_id)
        return Employee(**e) if e else None

    def update_employee(self, employee_id: int, payload: EmployeeUpdate) -> Optional[Employee]:
        e = self._employees.get(employee_id)
        if not e:
            return None
        update_data = payload.dict(exclude_unset=True)
        e.update(update_data)
        self._employees[employee_id] = e
        return Employee(**e)

    def delete_employee(self, employee_id: int) -> bool:
        if employee_id in self._employees:
            # also unassign tasks assigned to this employee
            for t in self._tasks.values():
                if t.get("assigned_to") == employee_id:
                    t["assigned_to"] = None
            del self._employees[employee_id]
            return True
        return False

    # Task operations
    def create_task(self, payload: TaskCreate) -> Task:
        t = payload.dict()
        t_id = self._next_task_id
        t["id"] = t_id
        # normalize status
        if isinstance(t.get("status"), TaskStatus):
            t["status"] = t["status"].value
        self._tasks[t_id] = t
        self._next_task_id += 1
        return Task(**t)

    def list_tasks(self, status: Optional[TaskStatus] = None, assigned_to: Optional[int] = None) -> List[Task]:
        out = []
        for t in self._tasks.values():
            if status and t.get("status") != status.value:
                continue
            if assigned_to is not None and t.get("assigned_to") != assigned_to:
                continue
            out.append(Task(**t))
        return out

    def get_task(self, task_id: int) -> Optional[Task]:
        t = self._tasks.get(task_id)
        return Task(**t) if t else None

    def update_task(self, task_id: int, payload: TaskUpdate) -> Optional[Task]:
        t = self._tasks.get(task_id)
        if not t:
            return None
        update_data = payload.dict(exclude_unset=True)
        if "status" in update_data and isinstance(update_data["status"], TaskStatus):
            update_data["status"] = update_data["status"].value
        t.update(update_data)
        self._tasks[task_id] = t
        return Task(**t)

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
