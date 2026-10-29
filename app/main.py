import pyodbc
from fastapi import FastAPI
from pydantic import BaseModel
class Task(BaseModel):
    title: str


def get_db_connection():
    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        r"SERVER=DESKTOP-MFUT2Q8\LSSQL;"
        "DATABASE=MissionUltronDB;"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)


app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "Mission Ultron",
        "status": "online"
    }
@app.post("/tasks")
def create_task(task: Task):
    return {"message": "Task received", "title": task.title}