from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import api_postgres.models as models
import api_postgres.schemas as schemas
import api_postgres.services as services
from api_postgres.db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.get("/book_by_id/", response_model=schemas.Book)
def read_book_by_id(id: int, db: Session = Depends(get_db)):
    book = services.get_book_by_id(db, id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{id}", status_code=200)
def delete_book(id: int, db: Session = Depends(get_db)):
    book = services.delete_book_by_id(db, id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted successfully"}