from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Interval

engine = create_engine("postgresql://nastya@localhost/testdb2")

"""Для создания моделей необходима базовая модель, от которой потом наследуются остальные модели
Классы, которые наследуются от класса базовой модели, будут сопоставляться с таблицами в базе данных. 
Для сопоставления класса с определенной таблицей в БД применяется атрибут класса __tablename__.
"""


class Base(DeclarativeBase):
    pass


class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String)


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    release_year = Column(Integer)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)

    artist = relationship("Artist", back_populates="albums")


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    duration = Column(Interval)
    album_id = Column(Integer, ForeignKey('albums.id'), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)

    artist = relationship("Artist", back_populates="songs")
    album = relationship("Album", back_populates="songs")


Base.metadata.create_all(bind=engine)
