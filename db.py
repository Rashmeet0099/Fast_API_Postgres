# File: api_postgres/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Use your real PostgreSQL credentials here:
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Rashmeet0099@localhost:5432/test1"

# ✅ DO NOT use connect_args for PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
