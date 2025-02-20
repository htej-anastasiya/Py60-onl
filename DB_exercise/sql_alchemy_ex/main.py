from datetime import datetime

from entities.albums.albums import AlbumsService
from entities.artists.artists import ArtistService
from entities.songs.songs import SongsService

while True:
    print("""
    Select action number from provided list:
    1 - GET artists list
    2 - GET albums list for selected singer/band
    3 - GET INFO about songs by album name
    4 - GET INFO about songs by song name
    5 - ADD artist,band
    6 - ADD album for selected artist
    7 - ADD song for selected artist and album
    8 - UPDATE song name
    9 - DELETE song by name
    10 - EXIT program
    """)
    action = int(input("Input an action number to start: "))

    if action == 1:
        artists = ArtistService()
        lst = artists.get_all_artists_list()
        for i in lst:
            print(f'"{i.name}", country {i.country}')
    elif action == 2:
        name = input("Input singer/band name to get albums list: ")
        albums = AlbumsService()
        lst_albums = albums.get_albums_list_by_artist_name(name)
        for i in lst_albums:
            print(f'"{i.name}" album was released in {i.release_year}')
    elif action == 3:
        name = input("Input album name to get songs list: ")
        songs = SongsService()
        songs_lst = songs.get_songs_list_by_album_name(name)
        if not songs_lst:
            print("Nothing was found. Please, try again")
        else:
            for song in songs_lst:
                print(f'{song.title}, {str(song.duration)} - from "{song.album.name}" album, by {song.artist.name}')
    elif action == 4:
        name = input("Input song name to find all matching info: ")
        songs = SongsService()
        songs_lst = songs.get_all_matching_elements_by_name(name)
        if not songs_lst:
            print("Nothing was found. Please, try again")
        else:
            for song in songs_lst:
                print(f'{song.title}, {str(song.duration)} - from "{song.album.name}" album, by {song.artist.name}')
    elif action == 5:
        band_name = input("Input band or artist name: ")
        band_country = input("Input band or artist country: ")
        artists = ArtistService()
        operation = artists.add_artist(band_name, band_country)
        print(f'"{operation.name}" was added')
    elif action == 6:
        album_name = input("Input album name: ")
        band_name = input("Input band or artist name: ")
        release_year = int(input("Input album's release year: "))
        albums = AlbumsService()
        albums.add_album_for_artist(band_name, album_name, release_year)
    elif action == 7:
        album_name = input("Input album name: ")
        band_name = input("Input band or artist name: ")
        song_name = input("Input song name: ")
        song_duration = input("Enter song duration (HH:MM:SS): ")
        dur_converted = datetime.strptime(song_duration, "%H:%M:%S").time()
        songs = SongsService()
        songs.add_song(song_name, song_duration, album_name, band_name)
    # elif action == 8:
    #     name = input("Find song name to update: ")
    #     old_names = select_songs_by_name(name)
    #     for i in old_names:
    #         print(f'Song "{i[1]}", {str(i[2])} - from "{i[3]}" album, by {i[4]}')
    #     while True:
    #         old_name = input("Input found song name: ")
    #         new_name = input("Input new song name: ")
    #         if not old_name or not new_name:
    #             print("Error: Song names cannot be empty. Try again.")
    #             continue
    #         else:
    #             update_song_title(old_name, new_name)
    #             break
    # elif action == 9:
    #     name = input("Find song name to delete: ")
    #     old_names = select_songs_by_name(name)
    #     if not old_names:
    #         print("Nothing was found. Please, try again")
    #     else:
    #         for i in old_names:
    #             print(f'Song "{i[1]}", {str(i[2])} - from "{i[3]}" album, by {i[4]}')
    #     while True:
    #         name = input("Input found song name to delete it: ")
    #         if not name:
    #             print("Error: Song name cannot be empty. Try again.")
    #             continue
    #         else:
    #             delete_song_by_title(name)
    #             break

    elif action == 10:
        print("Quit program")
        break
