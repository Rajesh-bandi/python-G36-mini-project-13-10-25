# Employee Task Tracker API

Small FastAPI app that manages employees and tasks in-memory.

Run:

```bash
$ python -m uvicorn task_tracker.main:app --reload
```

Docs:

- Open http://127.0.0.1:8000/docs for Swagger UI
- Open http://127.0.0.1:8000/redoc for ReDoc

Authentication:

- Protected endpoints require header `x-token: work123`

Routes:

- /employees: CRUD for employees
- /tasks: CRUD for tasks

Schemas and examples are available in the interactive docs.

Example requests (use header `x-token: work123` for protected endpoints):

Create employee:

```bash
curl -X POST "http://127.0.0.1:8000/employees/" -H "Content-Type: application/json" -H "x-token: work123" -d '{"name":"Alice","email":"alice@example.com","role":"Engineer"}'
```

Create task:

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" -H "Content-Type: application/json" -H "x-token: work123" -d '{"title":"Write report","description":"Monthly","assigned_to":1}'
```
