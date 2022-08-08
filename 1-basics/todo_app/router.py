from fastapi import APIRouter, Path
from todo_app.model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "To do added successfully"}

@todo_router.get("/todo")
async  def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_todo_item(todo_id: int = Path(..., title="id of the item"))-> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo":todo
            }
        return {
            "message": "The id you supplied doesn't exist"
        }