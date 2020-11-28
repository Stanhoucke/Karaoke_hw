import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from classes.drink import Drink

class TestRoom(unittest.TestCase):

    def setUp(self):
        # Drinks
        self.drink_1 = Drink("Tennents", 3.50, True)
        self.drink_2 = Drink("Coca Cola", 2.00, False)

        # Songs
        self.song_1 = Song("Shake It Off", "Taylor Swift", 219)
        self.song_2 = Song("Sweet Caroline", "Neil Diamond", 201)
        self.song_3 = Song("YMCA", "Village People", 287)

        # Guests
        self.guest_1 = Guest("Alice", 43, 30.00, self.song_3)
        self.guest_2 = Guest("Bob", 45, 60.00, self.song_3)
        self.guest_3 = Guest("Charlie", 21, 15.50, self.song_3)
        self.guest_4 = Guest("David", 17, 10.00, self.song_2)
        self.guest_5 = Guest("Emma", 24, 29.95, self.song_2)
        self.guest_6 = Guest("Freddie", 31, 5.00, self.song_1)

        group_1 = [self.guest_1, self.guest_2, self.guest_3, self.guest_4, self.guest_5]
    
        # Rooms
        self.room_1 = Room(1, 4)
        self.room_2 = Room(2, 5)

        self.room_2.guests = group_1

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

    def test_favourite_song_on_playlist__returns_message(self):
        self.room_1.add_song(self.song_3)
        self.assertEqual("Whoo!", self.room_1.favourite_song_on_playlist(self.guest_1))

    # Methods that affect number of guests in room
    def test_add_guest_to_room(self):
        self.room_1.add_guest(self.guest_1, self.room_1)
        self.assertEqual(1, len(self.room_1.guests))
    
    def test_add_guest_4_times__returns_guests_len_4(self):
        self.room_1.add_guest(self.guest_2, self.room_1)
        self.room_1.add_guest(self.guest_2, self.room_1)
        self.room_1.add_guest(self.guest_2, self.room_1)
        self.room_1.add_guest(self.guest_2, self.room_1)
        self.assertEqual(4, len(self.room_1.guests))
    
    def test_remove_guest_from_room(self):
        self.room_2.remove_guest(self.guest_3)
        self.assertEqual(4, len(self.room_2.guests))

    def test_remove_2_guests_from_room(self):
        self.room_2.remove_guest(self.guest_1)
        self.room_2.remove_guest(self.guest_5)
        self.assertEqual(3, len(self.room_2.guests))

    def test_add_guest__rejects_guest_cannot_afford_entry(self):
        self.room_1.add_guest(self.guest_1, self.room_1)
        self.room_1.add_guest(self.guest_6, self.room_1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_add_guest__rejects_guest_room_at_capacity(self):
        self.room_2.add_guest(self.guest_1, self.room_2)
        self.assertEqual(5, len(self.room_2.guests))

    # Methods that check room capacity
    def test_check_capacity_for_under_capacity__returns_True(self):
        has_capacity = self.room_1.check_capacity(self.room_1)
        self.assertEqual(True, has_capacity)

    def test_check_capacity_for_at_capacity__returns_False(self):
        at_capacity = self.room_2.check_capacity(self.room_2)
        self.assertEqual(False, at_capacity)

    # Methods that affect tab
    def test_add_drink_to_tab__adds_drink_price_to_tab(self):
        self.room_1.add_drink_to_tab(self.guest_2, self.drink_1)
        self.assertEqual(3.50, self.room_1.tab)
        self.assertEqual(56.50, self.guest_2.wallet)

    def test_add_entry_fee_to_tab__adds_entry_fee_to_tab(self):
        self.room_1.add_entry_fee_to_tab(self.guest_2)
        self.assertEqual(9.95, self.room_1.tab)
        self.assertEqual(50.05, self.guest_2.wallet)

    def test_clear_room__removes_guests_playlist_tab(self):
        self.room_1.add_guest(self.guest_2, self.room_1)
        self.assertEqual(1, len(self.room_1.guests))
        self.assertEqual(9.95, self.room_1.tab)
        self.assertEqual(50.05, self.guest_2.wallet)

        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.playlist))

        self.room_1.clear_room(self.room_1)
        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(0, len(self.room_1.playlist))
        self.assertEqual(0.00, self.room_1.tab)