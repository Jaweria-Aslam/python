# Song class
class Song:

    # Parameterized constructor
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


# Creating Song object and passing title and artist
song1 = Song("Perfect", "Ed Sheeran")

# Printing song details
print("Song Title:", song1.title)
print("Artist:", song1.artist)