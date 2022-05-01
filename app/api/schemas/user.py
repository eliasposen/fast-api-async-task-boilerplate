from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    username: str
    last_login: datetime

    class Config:
        orm_mode = True
