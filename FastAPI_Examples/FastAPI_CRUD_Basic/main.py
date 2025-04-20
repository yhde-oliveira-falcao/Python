from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"todos": "Todo has been added"}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_one_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "no todos found"}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_object: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = todo_object.item

            return {"message": f"Todo with id {todo.id} has been updated"}

    return {"message": "No todos found"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "todo has been deleted"}
    return {"message": "No todos found"}

