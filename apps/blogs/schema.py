from typing import Optional
from datetime import datetime, date

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]