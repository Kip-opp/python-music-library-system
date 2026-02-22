class Song:
    """
    Represents a song with name, artist, and genre attributes.
    Tracks class-level statistics for all song instances.
    """
    # Class attributes to track song statistics
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Initialize a new Song instance with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre
        # Update class-level statistics when a new song is created
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total count of Song instances."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the list of unique genres (if not already present)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the list of unique artists (if not already present)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Update the genre count dictionary with the given genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Update the artist count dictionary with the given artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
