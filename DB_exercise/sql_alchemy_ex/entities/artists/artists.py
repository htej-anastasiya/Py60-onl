from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from db_schema import Album, Artist, Song
from sqlalchemy.orm import Session

engine = create_engine("postgresql://nastya@localhost/testdb2")

def get_all_artists_list():
    with Session(bind=engine) as db_session:
        artists_list = db_session.query(Artist).all()
        return artists_list

# Add None check
def get_artist_id_by_name(name, db_session):
    artist_by_name = db_session.query(Artist).filter(Artist.name.ilike(name)).first()
    return artist_by_name.id

def update_artist_name(name, name_to_update):
    with Session(bind=engine) as db_session:
        artist_id = get_artist_id_by_name(name, db_session)
        artist_info = db_session.query(Artist).filter(Artist.id==artist_id).first()
        artist_info.name = name_to_update
        db_session.commit()
        db_session.refresh(artist_info)
        return artist_info.name

def update_artist_country(name, country_to_update):
    with Session(bind=engine) as db_session:
        artist_id = get_artist_id_by_name(name, db_session)
        artist_info = db_session.query(Artist).filter(Artist.id==artist_id).first()
        artist_info.country = country_to_update
        db_session.commit()
        db_session.refresh(artist_info)
        return artist_info.country

def add_artist(name,country):
    with Session(bind=engine) as db_session:
        artist = Artist(name=name, country=country)
        db_session.add(artist)
        db_session.commit()
        db_session.refresh(artist)
        return artist


# artists = get_all_artists_list()
# for artist in artists:
#     print(artist.name, artist.country)
artists = update_artist_country('Pantera', 'USA')
print(artists)

