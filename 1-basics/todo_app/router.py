from fastapi import APIRouter, Path, HTTPException, status, Request, Depends

from todo_app.model import Todo, TodoItem, TodoItems
from fastapi.templating import Jinja2Templates

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")


@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
        {
            "request": request,
            "todos": todo_list
        }
    )


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos(request: Request):
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })


@todo_router.get("/todo/{todo_id}")
async def get_todo_item(request: Request, todo_id: int = Path(..., title="id of the item")):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                "todo.html", {
                    "request": request,
                    "todo": todo
                }
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID does not exist"
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="Id of the item to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID does not exist"
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID does not exist"
    )


@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully"
    }
