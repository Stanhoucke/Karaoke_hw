import unittest
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):

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
        self.guest_6 = Guest("Freddie", 31, 5.00, self.song_1)

    # Class attribute tests
    def test_guest_has_name(self):
        self.assertEqual("Alice", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(43, self.guest_1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(30.00, self.guest_1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song_1, self.guest_6.favourite_song)

    # Methods that affect wallet
    def test_pay_entry_fee__reduces_amount_in_wallet(self):
        self.guest_1.pay_entry_fee()
        self.assertEqual(20.05, self.guest_1.wallet)

    def test_pay_entry_fee__accept_paying_guest(self):
        self.assertEqual(True, self.guest_1.pay_entry_fee())

    def test_pay_entry_fee__rejects_guest_cannot_afford_entry(self):
        self.guest_6.pay_entry_fee()
        self.assertEqual(5.00, self.guest_6.wallet)
        self.assertEqual(False, self.guest_6.pay_entry_fee())

    def test_pay_for_drink__removes_money_from_wallet(self):
        self.assertEqual(True, self.guest_6.pay_for_drink(self.drink_2))
        self.assertEqual(3.00, self.guest_6.wallet)

    def test_pay_for_drink__cannot_afford_drink(self):
        self.guest_6.pay_for_drink(self.drink_1)
        self.assertEqual(False, self.guest_6.pay_for_drink(self.drink_1))    
        self.assertEqual(1.50, self.guest_6.wallet)

    