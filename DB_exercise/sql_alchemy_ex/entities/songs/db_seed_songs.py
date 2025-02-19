from entities.albums.db_seed_albums import select_data
from db_schema import Album, Song
from entities.session_manager import DataBaseSessionManager

songs_data = [
    ('Battery', '00:03:12', 'Master of Puppets', 'Metallica'),
    ('Master of Puppets', '00:05:15', 'Master of Puppets', 'Metallica'),
    ('Welcome Home (Sanitarium)', '00:04:31', 'Master of Puppets', 'Metallica'),
    ('Disposable Heroes', '00:04:36', 'Master of Puppets', 'Metallica'),
    ('Orion', '00:04:38', 'Master of Puppets', 'Metallica'),
    ('Fight Fire with Fire', '00:02:24', 'Ride the Lightning', 'Metallica'),
    ('Ride the Lightning', '00:03:37', 'Ride the Lightning', 'Metallica'),
    ('Fade to Black', '00:06:58', 'Ride the Lightning', 'Metallica'),
    ('Creeping Death', '00:06:36', 'Ride the Lightning', 'Metallica'),
    ('The Call of Ktulu', '00:08:53', 'Ride the Lightning', 'Metallica'),
    ('Blackened', '00:06:17', '...And Justice for All', 'Metallica'),
    ('...And Justice for All', '00:09:48', '...And Justice for All', 'Metallica'),
    ('One', '00:07:27', '...And Justice for All', 'Metallica'),
    ('Harvester of Sorrow', '00:05:30', '...And Justice for All', 'Metallica'),
    ('Dyers Eve', '00:05:16', '...And Justice for All', 'Metallica'),
    ('Angel of Death', '00:04:46', 'Reign in Blood', 'Slayer'),
    ('Piece by Piece', '00:02:22', 'Reign in Blood', 'Slayer'),
    ('Necrophobic', '00:01:40', 'Reign in Blood', 'Slayer'),
    ('Altar of Sacrifice', '00:02:53', 'Reign in Blood', 'Slayer'),
    ('Jesus Saves', '00:02:51', 'Reign in Blood', 'Slayer'),
    ('War Ensemble', '00:04:58', 'Seasons in the Abyss', 'Slayer'),
    ('Blood Red', '00:04:04', 'Seasons in the Abyss', 'Slayer'),
    ('Spirit in Black', '00:04:26', 'Seasons in the Abyss', 'Slayer'),
    ('Expendable Youth', '00:04:11', 'Seasons in the Abyss', 'Slayer'),
    ('Dead Skin Mask', '00:05:11', 'Seasons in the Abyss', 'Slayer'),
    ('South of Heaven', '00:04:54', 'South of Heaven', 'Slayer'),
    ('Silent Scream', '00:03:48', 'South of Heaven', 'Slayer'),
    ('Live Undead', '00:03:36', 'South of Heaven', 'Slayer'),
    ('Behind the Crooked Cross', '00:04:18', 'South of Heaven', 'Slayer'),
    ('Mandatory Suicide', '00:04:41', 'South of Heaven', 'Slayer'),
    ('Cowboys from Hell', '00:04:24', 'Cowboys from Hell', 'Pantera'),
    ('Cemetery Gates', '00:07:15', 'Cowboys from Hell', 'Pantera'),
    ('Domination', '00:05:32', 'Cowboys from Hell', 'Pantera'),
    ('Psycho Holiday', '00:05:19', 'Cowboys from Hell', 'Pantera'),
    ('Shattered', '00:03:42', 'Cowboys from Hell', 'Pantera'),
    ('Mouth for War', '00:03:48', 'Vulgar Display of Power', 'Pantera'),
    ('Walk', '00:05:10', 'Vulgar Display of Power', 'Pantera'),
    ('This Love', '00:06:20', 'Vulgar Display of Power', 'Pantera'),
    ('Rise', '00:04:21', 'Vulgar Display of Power', 'Pantera'),
    ('Regular People (Conceit)', '00:05:15', 'Vulgar Display of Power', 'Pantera'),
    ('Strength Beyond Strength', '00:03:15', 'Far Beyond Driven', 'Pantera'),
    ('Becoming', '00:03:30', 'Far Beyond Driven', 'Pantera'),
    ('5 Minutes Alone', '00:05:16', 'Far Beyond Driven', 'Pantera'),
    ('I’m Broken', '00:04:31', 'Far Beyond Driven', 'Pantera'),
    ('Slaughtered', '00:03:43', 'Far Beyond Driven', 'Pantera'),
    ('(sic)', '00:03:34', 'Slipknot', 'Slipknot'),
    ('Eyeless', '00:03:50', 'Slipknot', 'Slipknot'),
    ('Wait and Bleed', '00:02:55', 'Slipknot', 'Slipknot'),
    ('Spit It Out', '00:02:58', 'Slipknot', 'Slipknot'),
    ('Surfacing', '00:03:56', 'Slipknot', 'Slipknot'),
    ('People = Shit', '00:03:35', 'Iowa', 'Slipknot'),
    ('Disasterpiece', '00:05:02', 'Iowa', 'Slipknot'),
    ('My Plague', '00:03:38', 'Iowa', 'Slipknot'),
    ('The Heretic Anthem', '00:04:10', 'Iowa', 'Slipknot'),
    ('Left Behind', '00:04:08', 'Iowa', 'Slipknot'),
    ('Duality', '00:04:04', 'Vol. 3: The Subliminal Verses', 'Slipknot'),
    ('Before I Forget', '00:04:21', 'Vol. 3: The Subliminal Verses', 'Slipknot'),
    ('Vermilion', '00:05:19', 'Vol. 3: The Subliminal Verses', 'Slipknot'),
    ('Pulse of the Maggots', '00:04:57', 'Vol. 3: The Subliminal Verses', 'Slipknot'),
    ('The Nameless', '00:04:52', 'Vol. 3: The Subliminal Verses', 'Slipknot'),
    ('Laid to Rest', '00:03:58', 'Ashes of the Wake', 'Lamb of God'),
    ('Hourglass', '00:04:17', 'Ashes of the Wake', 'Lamb of God'),
    ('Now You’ve Got Something to Die For', '00:03:52', 'Ashes of the Wake', 'Lamb of God'),
    ('Omerta', '00:04:48', 'Ashes of the Wake', 'Lamb of God'),
    ('Blood of the Scribe', '00:05:15', 'Ashes of the Wake', 'Lamb of God'),
    ('Born for One Thing', '00:04:16', 'Fortitude', 'Gojira'),
    ('Amazonia', '00:04:41', 'Fortitude', 'Gojira'),
    ('Another World', '00:04:34', 'Fortitude', 'Gojira'),
    ('Hold On', '00:05:12', 'Fortitude', 'Gojira'),
    ('The Chant', '00:05:30', 'Fortitude', 'Gojira'),
    ('Gravedigger’s Chant', '00:03:15', 'Stranger Fruit', 'Zeal & Ardor'),
    ('Servants', '00:03:16', 'Stranger Fruit', 'Zeal & Ardor'),
    ('Don’t You Dare', '00:03:43', 'Stranger Fruit', 'Zeal & Ardor'),
    ('Fire of Motion', '00:01:42', 'Stranger Fruit', 'Zeal & Ardor'),
    ('Waste', '00:02:38', 'Stranger Fruit', 'Zeal & Ardor')
]


def select_album_id_by_name(album):
    with DataBaseSessionManager() as db:
        album_name = db.query(Album).filter(Album.name == album).first()
        if album_name:
            return album_name.id
        return None


def insert_data(data):
    with DataBaseSessionManager() as db_session:
        for song_name, duration, album_name, artist_name in data:
            artist_id = select_data(artist_name)
            album_id = select_album_id_by_name(album_name)
            if album_id and artist_id:
                new_song = Song(title=song_name, duration=duration, album_id=album_id, artist_id=artist_id)
                db_session.add(new_song)
            else:
                print(f"Artist '{artist_name}' and {album_name} not found. Skipping song '{song_name}'.")
            db_session.commit()
        print("Data was successfully inserted into DB")

if __name__ == "__main__":
    insert_data(songs_data)

# print(select_album_id_by_name('Stranger Fruit'))
