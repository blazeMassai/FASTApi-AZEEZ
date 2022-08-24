# from pydantic import BaseModel, EmailStr

from pydantic import EmailStr
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@rm.com",
                "password": "strong!!!",
            }
        }


class UserUpdate(SQLModel):
    email: Optional[str]
    password: Optional[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@rm.com",
                "password": "strong!!!",
            }
        }

# class User(BaseModel):
#     email: EmailStr
#     password: str
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "fastapi@rm.com",
#                 "password": "strong!!!",
#             }
#         }


class UserSignIn(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr
    password: str


# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str
#
#     schema_extra = {
#         "example": {
#             "email": "fastapi@rm.com",
#             "password": "strong!!!"
#         }
#     }
