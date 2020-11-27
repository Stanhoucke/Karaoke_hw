import unittest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1)

        self.song_1 = Song("Shake It Off", "Taylor Swift", 219)

    # Class attribute tests
    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_empty_playlist(self):
        self.assertEqual(0, len(self.room_1.playlist))

    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room_1.guests))

    # Methods that affect playlist
    def test_song_added_to_playlist(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_add_song_3_times__returns_playlist_len_3(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_1)
        self.assertEqual(3, len(self.room_1.playlist))
