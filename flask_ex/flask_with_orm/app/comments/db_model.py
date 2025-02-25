from app.base.baseservice import BaseService
from app.base.db_connection import Base
from sqlalchemy import create_engine, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Interval, DateTime



class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    content = Column(String)
    created_at = Column(DateTime)
    post = relationship('Post', back_populates='comments')


