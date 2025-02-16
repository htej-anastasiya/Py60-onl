from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from db_schema import Album, Artist, Song
from sqlalchemy.orm import Session

engine = create_engine("postgresql://nastya@localhost/testdb2")

artists_data = [
    Artist(name='Metallica', country='USA'),
    Artist(name='Slayer', country='USA'),
    Artist(name='Pantera', country='USA'),
    Artist(name='Slipknot', country='USA'),
    Artist(name='Lamb of God', country='USA'),
    Artist(name='Gojira', country='France'),
    Artist(name='In Flames', country='Sweden'),
    Artist(name='Children of Bodom', country='Finland'),
    Artist(name='Nightwish', country='Finland'),
    Artist(name='System of a Down', country='USA'),
    Artist(name='Arch Enemy', country='Sweden'),
    Artist(name='Behemoth', country='Poland'),
    Artist(name='Sepultura', country='Brazil'),
    Artist(name='Zeal & Ardor', country='Switzerland')
]


#function which creates session for DB connection, inserts data  with Exception SQLAlchemyError
def insert_data(data):
    with Session(autoflush=False, bind=engine) as db:
        try:
            db.add_all(data)
            db.commit()
            print("Data was inserted into DB")
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error during data insertion {e}")
        finally:
            db.close()


if __name__ == "__main__":
    insert_data(artists_data)

