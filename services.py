from sqlalchemy.orm import Session
import api_postgres.models as models
import api_postgres.schemas as schemas

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def delete_book_by_id(db: Session, id: int):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if book:
        db.delete(book)
        db.commit()
    return book