from pydantic import BaseModel

class UserBase(Basemodel):
    email: EmailStr
    username: str

class UserCreate(userBase):
    password: str

class User(UserBase):
    id: int