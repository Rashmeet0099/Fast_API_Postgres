from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api_postgres import models, schemas, services
from api_postgres.db import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/books/", response_model=list[schemas.Book])
def get_all_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.post("/books/", response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)
