from typing import Optional
from datetime import datetime, date

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True
