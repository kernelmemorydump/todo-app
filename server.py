import uvicorn
import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel

db_config = {
    "host": "localhost",
    "user": "mysql",
    "password": "mysql",
    "database": "todo",
}

class Todo(BaseModel):
    id: int
    naziv: str
    zavrseno: bool


class CreateOrEditTodo(BaseModel):
    naziv: str
    zavrseno: bool


app = FastAPI()

@app.get("/")
async def prikazi_todos():
    """Prikazuje sve postojece zadtke."""
    try:
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM todo_tasks")

        tasks = db_cursor.fetchall()

        db_cursor.close()
        db_connection.close()

        return { "tasks": tasks }
    except mysql.connector.Error as err:
        return { "error", err }

@app.post("/")
async def novi_todo(todo: CreateOrEditTodo):
    """Kreaira novi todo zadatak."""
    naziv = todo.naziv
    zavrseno = 1 if todo.zavrseno else 0

    try:
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()

        db_cursor.execute(f"INSERT INTO todo_tasks (id, ime, zavrseno) VALUES (0, '{naziv}', {zavrseno})")
        db_connection.commit()

        db_cursor.close()
        db_connection.close()
    except mysql.connector.Error as err:
        return { "error", err }

@app.put("/zavrsi")
async def zavrsi_todo(id: int):
    """Zavrsava postojeci zadatak."""
    try:
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()

        complete_query = f"UPDATE todo_tasks SET zavrseno = 1 WHERE id = {id}"
        db_cursor.execute(complete_query)
        db_connection.commit()
        
        db_cursor.close()
        db_connection.close()
    except mysql.connector.Error as err:
        return { "error", err }

@app.put("/")
async def izmeni_todo(id: int, todo: CreateOrEditTodo):
    """Menja već postojeći todo."""
    zavrseno = 1 if todo.zavrseno else 0

    try:
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()

        print(todo)
        update_query = f"UPDATE todo_tasks SET ime = '{todo.naziv}', zavrseno = {zavrseno} WHERE id = {id}"
        db_cursor.execute(update_query)
        db_connection.commit()
        
        db_cursor.close()
        db_connection.close()
    except mysql.connector.Error as err:
        return { "error", err }

@app.delete("/")
async def obrisi_todo(id: int):
    """Briše već postojeći zadatak."""
    try:
        db_connection = mysql.connector.connect(**db_config)
        db_cursor = db_connection.cursor()

        delete_query = f"DELETE FROM todo_tasks WHERE id = {id}"
        db_cursor.execute(delete_query)
        db_connection.commit()
        
        db_cursor.close()
        db_connection.close()
    except mysql.connector.Error as err:
        return { "error", err }
    

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")