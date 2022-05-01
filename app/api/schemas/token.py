from lib2to3.pytree import Base

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
