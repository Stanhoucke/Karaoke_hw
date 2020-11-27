import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Shake It Off", "Taylor Swift", 219)

    # Class attribute tests
    def test_song_has_title(self):
        self.assertEqual("Shake It Off", self.song_1.song_title)

    def test_song_has_artist(self):
        self.assertEqual("Taylor Swift", self.song_1.artist_name)

    def test_song_has_length(self):
        self.assertEqual(219, self.song_1.length_seconds)
    