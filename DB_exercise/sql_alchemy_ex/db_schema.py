from sqlalchemy import create_engine, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Interval
from entities.connection_strings import engine


class Base(DeclarativeBase):
    pass


class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String)

    albums = relationship("Album", back_populates="artist")
    songs = relationship("Song", back_populates="artist")
    __table_args__ = (UniqueConstraint('name', name='uq_artist_name'),)


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    release_year = Column(Integer)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)

    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")
    __table_args__ = (UniqueConstraint('artist_id', 'name', name='uq_album_artist_name'),)


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    duration = Column(Interval)
    album_id = Column(Integer, ForeignKey('albums.id'), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)

    artist = relationship("Artist", back_populates="songs")
    album = relationship("Album", back_populates="songs")


# Base.metadata.create_all(bind=engine)
