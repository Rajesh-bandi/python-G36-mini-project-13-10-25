from fastapi import FastAPI
from .routers import employees, tasks

app = FastAPI(title="Employee Task Tracker API",
              description="A small FastAPI app to manage employees and their tasks.",
              version="0.1.0")

app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


@app.get("/", summary="Root")
async def root():
    return {"message": "Employee Task Tracker API. Visit /docs for interactive docs."}
