from datetime import datetime
from db_connect import DbConnection

def select_songs_from_album(query):
    with DbConnection() as cursor:
        sql_query = """
            SELECT songs.id, songs.title, songs.duration, a.name, art.name AS album_name
            FROM songs
            JOIN albums a ON songs.album_id = a.id
            JOIN artists art ON art.id = a.artist_id
            WHERE a.name ILIKE %s
        """
        # print(f" SQL Запрос: {sql_query} с параметром: {query}")
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
        sql_query = """
        Insert into artists (name, country) values (%s,%s);
        """
        cursor.execute(sql_query, (name, country))
        print(f"Artist '{name}' added successfully.")

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
            album_exists = cursor.fetchone()
            if album_exists:
                print (f"Song '{title}' by '{artist_name}' in the album '{album_name}' is already exists.")
                return
            else:
                sql_query = """
                INSERT INTO songs (title, duration, album_id, artist_id)
                VALUES (%s,%s,(SELECT id FROM albums WHERE name = %s),
                (SELECT id FROM artists WHERE name = %s));
                """
                cursor.execute(sql_query, (title, duration, album_name, artist_name))
                print(f"Song '{title}' is added successfully.")
        except Exception as ex:
            print(f"Song '{ex}' is already exists")
