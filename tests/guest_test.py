import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Alice", 43, 30.00)

    # Class attribute tests
    def test_guest_has_name(self):
        self.assertEqual("Alice", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(43, self.guest_1.age)

    # Methods that affect wallet
    def test_pay_entry_fee__reduces_amount_in_wallet(self):
        self.guest_1.pay_entry_fee()
        self.assertEqual(20.05, self.guest_1.wallet)