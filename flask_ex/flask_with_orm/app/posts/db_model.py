from app.base.baseservice import BaseService
from app.base.db_connection import Base
from sqlalchemy import create_engine, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Interval, DateTime



class Post(Base):
    __tablename__="posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    author_id = Column(Integer)
    comments = relationship('Comment', back_populates='posts')

    __table_args__ = (UniqueConstraint('title', name='uq_post_title'),)

