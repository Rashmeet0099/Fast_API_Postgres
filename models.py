# File: api_postgres/models.py
from sqlalchemy import Column, Integer, String
from api_postgres.db import Base  # ✅ Make sure Base is imported from correct file

class Book(Base):  # ✅ This should inherit from Base
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, index=True)
    year = Column(Integer)
