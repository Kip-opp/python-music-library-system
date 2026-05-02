# Music Library System Lab

This project implements a `Song` class in Python to model tracks in a music library system. Each song stores its own `name`, `artist`, and `genre`, while the class also maintains shared statistics such as total songs created, unique artists, unique genres, and per-artist/per-genre counts. Clear project descriptions, setup steps, and usage examples are standard README practice for Python projects. [web:254][web:260]

## Overview

The goal of this lab is to practice:

- instance attributes
- class attributes
- class methods
- clean object-oriented design

When a new `Song` instance is created, the class should automatically update global music library statistics. Class attributes are intended for exactly this kind of shared state across all instances. [web:277][web:281][web:284]

## Song Model

### Instance Attributes
- `name`
- `artist`
- `genre`

### Class Attributes
- `count` — total number of songs created
- `genres` — unique list of genres
- `artists` — unique list of artists
- `genre_count` — dictionary of songs per genre
- `artist_count` — dictionary of songs per artist

### Class Methods
- `add_song_to_count()`
- `add_to_genres(genre)`
- `add_to_artists(artist)`
- `add_to_genre_count(genre)`
- `add_to_artist_count(artist)`

Each of these methods should be triggered automatically inside `__init__` whenever a new song is created. [web:279][web:284]

## Setup

Clone the repository, open it in VS Code, and install dependencies:

```bash
npm install
```

Create a feature branch before starting work:

```bash
git checkout -b feat/song-class
```

## Testing

Run the test suite with:

```bash
python -m pytest lib/testing/song_test.py -v
```

## Example Usage

```python
from song import Song

song1 = Song("Halo", "Beyonce", "Pop")
song2 = Song("Empire State of Mind", "Jay-Z", "Rap")
song3 = Song("Single Ladies", "Beyonce", "Pop")

print(Song.count)         # 3
print(Song.genres)        # ["Pop", "Rap"]
print(Song.artists)       # ["Beyonce", "Jay-Z"]
print(Song.genre_count)   # {"Pop": 2, "Rap": 1}
print(Song.artist_count)  # {"Beyonce": 2, "Jay-Z": 1}
```

## Workflow

After implementation:

```bash
git add .
git commit -m "feat: implement Song class with class attributes and class methods"
git push origin feat/song-class
```
