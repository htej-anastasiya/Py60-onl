from sqlalchemy.exc import SQLAlchemyError
from db_schema import Artist
from sqlalchemy.orm import Session
from entities.connection_strings import SessionLocal


class ArtistService:
    @staticmethod
    def get_all_artists_list():
        with SessionLocal() as db_session:
            artists_list = db_session.query(Artist).all()
            return artists_list

    @staticmethod
    def get_artist_id_by_name(name, db_session):
        artist_by_name = db_session.query(Artist).filter(Artist.name.ilike(f"%{name}%")).first()
        if not artist_by_name:
            return None
        return artist_by_name.id

    def update_artist_name(self, name, name_to_update):
        with SessionLocal() as db_session:
            artist_id = self.get_artist_id_by_name(name, db_session)
            if artist_id is None:
                return f"Nothing was found for '{name}'"
            else:
                artist_info = db_session.query(Artist).filter(Artist.id == artist_id).first()
                artist_info.name = name_to_update
                db_session.commit()
                db_session.refresh(artist_info)
                return artist_info.name

    def update_artist_country(self, name, country_to_update):
        with SessionLocal() as db_session:
            artist_id = self.get_artist_id_by_name(name, db_session)
            if artist_id is None:
                return f"Nothing was found for '{name}'"
            else:
                artist_info = db_session.query(Artist).filter(Artist.id == artist_id).first()
                artist_info.country = country_to_update
                db_session.commit()
                db_session.refresh(artist_info)
                return artist_info.country

    @staticmethod
    def add_artist(name, country):
        try:
            with SessionLocal() as db_session:
                artist = Artist(name=name, country=country)
                db_session.add(artist)
                db_session.commit()
                db_session.refresh(artist)
                return artist
        except SQLAlchemyError as e:
            print(f'Error while adding artist: {e}')

