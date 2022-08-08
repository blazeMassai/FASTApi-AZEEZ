# Models are created by subclassing Pydantic’s BaseModel class
# Pydantic is a Python library that handles data validation using Python-type annotations.

from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str