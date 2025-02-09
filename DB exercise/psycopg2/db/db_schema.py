import psycopg2
from psycopg2 import connect

from config import DB_CONFIG

"""Song (id, title, duration, album_id, artist_id)
Album (id, name, release_year)
Artist (id, name, country)"""


def create_tables():
    commands = [
        """
        Create table if not exists artists(
        id Serial Primary key,
        name varchar(255),
        country varchar(255)
        );
        """,
        """
        Create table if not exists albums(
        id Serial Primary key,
        name varchar(255),
        release_year int,
        artist_id int,
        constraint fk_artist_id foreign key (artist_id) REFERENCES artists(id)
        );
        """,
        """
        Create table if not exists songs(
        id Serial Primary key,
        title varchar(255),
        duration time,
        artist_id int,
        album_id int,
        constraint fk_artist_id foreign key (artist_id) REFERENCES artists(id),
        constraint fk_album_id foreign key (album_id) REFERENCES albums(id)
        );
        """
    ]

    try:
        with psycopg2.connect(**DB_CONFIG) as connect_db:
            with connect_db.cursor() as cursor:
                for command in commands:
                    cursor.execute(command)
            connect_db.commit()
    except Exception as ex:
        print(f"Error with creation {ex}")


if __name__ == "__main__":
    create_tables()
