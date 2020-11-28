import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Tennents", 3.50, True)
        self.drink_2 = Drink("Coca Cola", 2.00, False)

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink_1.price)

    def test_drink_has_alcoholic(self):
        self.assertEqual(True, self.drink_1.alcoholic)
        self.assertEqual(False, self.drink_2.alcoholic)

