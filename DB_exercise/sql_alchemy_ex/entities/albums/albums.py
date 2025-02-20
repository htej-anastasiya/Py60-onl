from sqlalchemy.exc import SQLAlchemyError
from db_schema import Album
from entities.connection_strings import SessionLocal
from entities.artists.artists import ArtistService


class AlbumsService:

    @staticmethod
    def get_albums_list_by_artist_name(artist_name):
        with SessionLocal() as db_session:
            artist_id = ArtistService.get_artist_id_by_name(artist_name,db_session)
            albums_list = db_session.query(Album).filter(Album.artist_id==artist_id)
            return albums_list

    @staticmethod
    def add_album_for_artist(artist_name, new_album_name, release_year):
        with SessionLocal() as db_session:
            try:
                artist_id = ArtistService.get_artist_id_by_name(artist_name, db_session)
                if artist_id is None:
                    raise SQLAlchemyError
                else:
                    album = Album(name=new_album_name, release_year=release_year, artist_id=artist_id)
                    db_session.add(album)
                    db_session.commit()
                    db_session.refresh(album)
                    return album
            except SQLAlchemyError:
                print(f'Error while adding album: {new_album_name}. Please, check if artist exists, if not - add artist first')

