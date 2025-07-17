# File: api_postgres/schemas.py

from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int

class BookCreate(BookBase):
    id: int  # <-- required from user when creating

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
