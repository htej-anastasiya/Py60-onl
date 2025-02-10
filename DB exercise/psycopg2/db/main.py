from datetime import datetime
from db_queries import select_songs_from_album, select_songs_by_name, add_artist, add_album, add_song

while True:
    print("""
    Select action number from provided list:
    1 - GET INFO about songs by album name
    2 - GET INFO about songs by song name
    3 - ADD artist,band
    4 - ADD album for selected artist
    5 - ADD song for selected artist and album
    6 - EXIT program
    """)
    action = int(input("Input an action number to start: "))

    if action == 1:
        name = input("Input album name to get songs list: ")
        albums = select_songs_from_album(name)
        for album in albums:
            print(f'{album[1]}, {str(album[2])} - from "{album[3]}" album, by {album[4]}')
    elif action == 2:
        name = input("Input song name to find all matching info: ")
        songs = select_songs_by_name(name)
        for i in songs:
            print(f'{i[1]}, {str(i[2])} - from "{i[3]}" album, by {i[4]}')
    elif action == 3:
        band_name = input("Input band or artist name: ")
        band_country = input("Input band or artist country: ")
        add_artist(band_name, band_country)
    elif action == 4:
        album_name = input("Input album name: ")
        band_name = input("Input band or artist name: ")
        release_year = int(input("Input album's release year: "))
        add_album(album_name, release_year, band_name)
    elif action == 5:
        album_name = input("Input album name: ")
        band_name = input("Input band or artist name: ")
        song_name = input("Input song name: ")
        song_duration = input("Enter song duration (HH:MM:SS): ")
        dur_converted = datetime.strptime(song_duration, "%H:%M:%S").time()
        add_song(song_name, song_duration, album_name, band_name)
    elif action == 6:
        print("Quit program")
        break
