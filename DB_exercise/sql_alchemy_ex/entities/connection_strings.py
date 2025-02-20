from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://nastya@localhost/testdb2"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)