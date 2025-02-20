from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from db_schema import Album, Song, Artist
from entities.connection_strings import SessionLocal
from entities.artists.artists import ArtistService
from entities.albums.albums import AlbumsService


class SongsService:

    @staticmethod
    def get_songs_list_by_album_name(album_name):
        with SessionLocal() as db_session:
            album_info = db_session.query(Album).filter(Album.name.ilike(f"%{album_name}%")).first()
            songs_list = db_session.query(Song).filter(Song.album_id == album_info.id)
            return songs_list

    @staticmethod
    def get_all_matching_elements_by_name(song_name):
        with (SessionLocal() as db_session):
            songs_list = (db_session.query(Song).filter(Song.title.ilike(f"%{song_name}%"))
                          .options(joinedload(Song.album), joinedload(Song.artist)).all())  # эту часть гуглила
            return songs_list

    @staticmethod
    def add_song(song_name, song_duration, album_name, band_name):
        with SessionLocal() as db_session:
            try:
                album_info = db_session.query(Album).filter(Album.name.ilike(f"%{album_name}%")).first()
                artist_info = db_session.query(Artist).filter(Artist.name.ilike(f"%{band_name}%")).first()
                if not album_info or not artist_info:
                    raise SQLAlchemyError
                else:
                    new_song = Song(title=song_name, duration=song_duration, album_id=album_info.id,
                                    artist_id=artist_info.id)
                    db_session.add(new_song)
                    db_session.commit()
                    db_session.refresh(new_song)
                    return new_song
            except SQLAlchemyError as e:
                print(f'An error has occurred {e}')


