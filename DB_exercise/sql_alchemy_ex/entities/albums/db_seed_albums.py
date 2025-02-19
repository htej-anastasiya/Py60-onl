from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from db_schema import Album, Artist, Song
from sqlalchemy.orm import Session
from entities.session_manager import DataBaseSessionManager

albums_data = [
    ('Master of Puppets', 1986, 'Metallica'),
    ('Ride the Lightning', 1984, 'Metallica'),
    ('...And Justice for All', 1988, 'Metallica'),
    ('Reign in Blood', 1986, 'Slayer'),
    ('Seasons in the Abyss', 1990, 'Slayer'),
    ('South of Heaven', 1988, 'Slayer'),
    ('Cowboys from Hell', 1990, 'Pantera'),
    ('Vulgar Display of Power', 1992, 'Pantera'),
    ('Far Beyond Driven', 1994, 'Pantera'),
    ('Slipknot', 1999, 'Slipknot'),
    ('Iowa', 2001, 'Slipknot'),
    ('Vol. 3: The Subliminal Verses', 2004, 'Slipknot'),
    ('Ashes of the Wake', 2004, 'Lamb of God'),
    ('Sacrament', 2006, 'Lamb of God'),
    ('Wrath', 2009, 'Lamb of God'),
    ("L''Enfant Sauvage", 2012, 'Gojira'),
    ('Magma', 2016, 'Gojira'),
    ('Fortitude', 2021, 'Gojira'),
    ('Clayman', 2000, 'In Flames'),
    ('Come Clarity', 2006, 'In Flames'),
    ('I, the Mask', 2019, 'In Flames'),
    ('Hatebreeder', 1999, 'Children of Bodom'),
    ('Follow the Reaper', 2000, 'Children of Bodom'),
    ('Halo of Blood', 2013, 'Children of Bodom'),
    ('Oceanborn', 1998, 'Nightwish'),
    ('Once', 2004, 'Nightwish'),
    ('Endless Forms Most Beautiful', 2015, 'Nightwish'),
    ('Toxicity', 2001, 'System of a Down'),
    ('Mezmerize', 2005, 'System of a Down'),
    ('Hypnotize', 2005, 'System of a Down'),
    ('Wages of Sin', 2001, 'Arch Enemy'),
    ('Doomsday Machine', 2005, 'Arch Enemy'),
    ('Deceivers', 2022, 'Arch Enemy'),
    ('Demigod', 2004, 'Behemoth'),
    ('The Satanist', 2014, 'Behemoth'),
    ('Opvs Contra Natvram', 2022, 'Behemoth'),
    ('Chaos A.D.', 1993, 'Sepultura'),
    ('Roots', 1996, 'Sepultura'),
    ('Machine Messiah', 2017, 'Sepultura'),
    ('Stranger Fruit', 2018, 'Zeal & Ardor'),
    ('Wake of a Nation', 2020, 'Zeal & Ardor'),
    ('Zeal & Ardor', 2022, 'Zeal & Ardor'),
]


def select_data(artist):
    with DataBaseSessionManager() as db_session:
        artist = db_session.query(Artist).filter(Artist.name == artist).first()
        if artist:
            return artist.id
        else:
            return None

def insert_data(data):
    with DataBaseSessionManager() as db_session:
        for album_name, release_year, artist_name in albums_data:
            artist_id=select_data(artist_name)
            if artist_id:
                new_album = Album(name=album_name, release_year=release_year, artist_id=artist_id)
                db_session.add(new_album)
            else:
                print(f"Artist '{artist_name}' not found. Skipping album '{album_name}'.")
            db_session.commit()
        print("Data was successfully inserted into DB")


if __name__ == "__main__":
    insert_data(albums_data)