from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    naziv: str
    zavrseno: bool


class EditTodo(BaseModel):
    naziv: str
    zavrseno: bool


app = FastAPI()

todos = [
    { "id": 0, "naziv": "Oprati sudove", "zavrseno": True },
    { "id": 1, "naziv": "Izbaciti smece", "zavrseno": False },
    { "id": 2, "naziv": "Spremiti rucak", "zavrseno": False },
    { "id": 3, "naziv": "Nauciti liste i dictionary-je", "zavrseno": True },
]

@app.get("/")
async def prikazi_todos():
    return todos

@app.post("/")
async def novi_todo(todo: Todo):
    print(todo)
    todos.append(todo)
    return { "message": "Novi todo je napravljen uspesno" }

@app.put("/")
async def izmeni_todo(id: int, todo: EditTodo):
    for existing_todo in todos:
        # print("Existing:", existing_todo["id"], "New:", id)

        if existing_todo["id"] == id:
            todo["id"] = id
            todos.remove(existing_todo)
            todos.append(todo)

            return { "message": f"Uspesno izmenjen todo {id}" }
        
        return { "message": f"Todo sa id-em {id} ne postoji!" }

@app.delete("/")
async def obrisi_todo(id: int):
    for existing_todo in todos:
        if existing_todo["id"] == id:
            todos.remove(existing_todo)

            return { "message": f"Todo {id} je uspesno obrisan" }
