import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Alice", 38)

    # Class attribute tests
    def test_guest_has_name(self):
        self.assertEqual("Alice", self.guest_1.name)