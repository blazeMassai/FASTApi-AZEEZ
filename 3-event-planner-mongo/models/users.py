from pydantic import BaseModel, EmailStr

from pydantic import EmailStr

class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@rm.com",
                "password": "strong!!!",
            }
        }



class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    schema_extra = {
        "example": {
            "email": "fastapi@rm.com",
            "password": "strong!!!"
        }
    }
