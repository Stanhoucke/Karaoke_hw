import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1)

    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_empty_playlist(self):
        self.assertEqual(0, len(self.room_1.playlist))

    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room_1.guests))