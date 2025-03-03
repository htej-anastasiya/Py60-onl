from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

DATABASE_URL = "postgresql://nastya@localhost/blog_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass
