from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode=True


class UserRead(BaseModel):
    id: int
    username: str
    email: str
    

class UserSelfRead(UserRead):
    balance: str