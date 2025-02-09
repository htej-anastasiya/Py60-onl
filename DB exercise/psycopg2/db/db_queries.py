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


name = input("Input album name to get songs list: ")
albums = select_songs_by_name(name)
for album in albums:
    print(f'{album[1]}, {str(album[2])} - "{album[3]}", {album[4]}')

