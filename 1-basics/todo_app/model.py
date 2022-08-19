# Models are created by subclassing Pydantic’s BaseModel class
# Pydantic is a Python library that handles data validation using Python-type annotations.
from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...)
    ):
        return cls(item=item)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!."
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Read"
                    },
                    {
                        "item": "Pray"
                    }
                ]
            }
        }
