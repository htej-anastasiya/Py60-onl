from datetime import datetime
from db.db_connect import DbConnection

def select_songs_from_album(query):
    with DbConnection() as cursor:
        sql_query = """
            SELECT songs.id, songs.title, songs.duration, a.name, art.name AS album_name
            FROM songs
            JOIN albums a ON songs.album_id = a.id
            JOIN artists art ON art.id = a.artist_id
            WHERE a.name ILIKE %s
        """
        # print(f" SQL query: {sql_query} с param: {query}")
        cursor.execute(sql_query,(f"%{query}%",))
        return cursor.fetchall()


def select_songs_by_name(query):
    with DbConnection() as cursor:
        sql_query = """
            SELECT songs.id, songs.title, songs.duration, a.name, art.name AS album_name
            FROM songs
            JOIN albums a ON songs.album_id = a.id
            JOIN artists art ON art.id = a.artist_id
            WHERE songs.title ILIKE %s
        """
        cursor.execute(sql_query,(f"%{query}%",))
        return cursor.fetchall()

def add_artist(name, country):
    with DbConnection() as cursor:
        try:
            check_artist = """
            Select * from artists where name = %s;
            """
            cursor.execute(check_artist, (name,))
            artist_exist = cursor.fetchone()
            if artist_exist:
                print(f"Artist '{name}' already exists.")
                return
            else:
                sql_query = """
                Insert into artists (name, country) values (%s,%s);
                """
                cursor.execute(sql_query, (name, country))
                cursor.connection.commit()
                print(f"Artist '{name}' added successfully.")
        except Exception as ex:
            print(f"Artist '{ex}' already exists")


def add_album(album_name, release_year, artist_name):
    with DbConnection() as cursor:
        try:
            check_album = """
            Select * from  albums where name = %s 
            AND artist_id = (SELECT id FROM artists WHERE name = %s);
            """
            cursor.execute(check_album,(f"%{album_name}%",f"%{album_name}%"))
            album_exists = cursor.fetchone()
            if album_exists:
                print (f"Album '{album_name}' by {artist_name} already exists.")
                return
            else:
                sql_query = """
                INSERT INTO albums (name, release_year, artist_id) 
                VALUES (%s,%s,(SELECT id FROM artists WHERE name = %s));
                """
                cursor.execute(sql_query, (album_name, release_year, artist_name))
                cursor.connection.commit()
                print(f"Album '{album_name}' added successfully.")
        except Exception as ex:
            print(f"Album '{ex}' already exists")

def add_song(title, duration, album_name, artist_name):
    with DbConnection() as cursor:
        try:
            check_song = """
            Select * from  songs where title ilike %s 
            AND artist_id = (SELECT id FROM artists WHERE name ilike %s);
            """
            cursor.execute(check_song,(f"%{title}%",f"%{artist_name}%"))
            song_exists = cursor.fetchone()
            if song_exists:
                print (f"Song '{title}' by '{artist_name}' in the album '{album_name}' is already exists.")
                return
            else:
                sql_query = """
                INSERT INTO songs (title, duration, album_id, artist_id)
                VALUES (%s,%s,(SELECT id FROM albums WHERE name = %s),
                (SELECT id FROM artists WHERE name = %s));
                """
                cursor.execute(sql_query, (title, duration, album_name, artist_name))
                cursor.connection.commit()
                print(f"Song '{title}' is added successfully.")
        except Exception as ex:
            print(f"Song '{ex}' is already exists")

def update_song_title(old_name, name):
    with DbConnection() as cursor:
        update_query = """
        Update songs
        set title = %s 
        where title = %s;
        """
        cursor.execute(update_query, (name,old_name))
        cursor.connection.commit()
        print(f"Song title '{old_name}' was updated to '{name}'.")

def delete_song_by_title(name):
    with DbConnection() as cursor:
        update_query = """
        DELETE FROM songs WHERE title = %s;
        """
        cursor.execute(update_query, (name,))
        cursor.connection.commit()
        print(f"Song '{name}' was deleted.")


def get_artists_list():
    with DbConnection() as cursor:
        query = """
        select * from artists;
        """
        cursor.execute(query)
        return cursor.fetchall()

def get_albums_by_band_name(name):
    with DbConnection() as cursor:
        query ="""
        SELECT albums.name, albums.release_year, artists.name 
            From albums
            JOIN artists 
			    ON artists.id = albums.artist_id
            WHERE artists.name ILIKE %s;
        """
        cursor.execute(query, (f"%{name}%",))
        return cursor.fetchall()