class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}

    def __init__(self, name, genre, artist):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)

    
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    def __str__(self):
        return f"Song: '{self.name}' by {self.artist} - Genre: {self.genre}"

# song1= Song("All of Me", "R&B", "John Legend")
# song2 = Song("Hey Jude", "Rock", "The Beatles")

# print(Song.count)          
# print(Song.genres)         
# print(Song.artists)        
# print(Song.genre_count)     