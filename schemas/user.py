from fastapi import UploadFile
from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str

class UserPayload(BaseUser):
    password: str

class UserResponse(BaseUser):
    pass

class LoginPayload(BaseModel):
    username: str
    password: str
    image: UploadFile

    model_config = {"extra": "forbid"}