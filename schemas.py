from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str
    year: int = 2024

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True  # Correct attribute
