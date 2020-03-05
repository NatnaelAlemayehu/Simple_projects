# Author: Natnael Alemayehu

# This file contains the test for the drink class

import unittest
from drink_class import Drink


# Class testing case
class TestCaseMethod(unittest.TestCase):
    def test_init(self):
        # Testing if init method is working
        drink_item = Drink("coca", 120, 30, 50, "cold soft drink")
        self.assertEqual(drink_item.name, 'coca')

    def test_init_second(self):
        # when empty arguments are passed to constructor
        self.assertRaises(ValueError, Drink, "",
                          "", "", "", "")

        # Testing when negative argument values are passed to constructor for some arguments

    def test_init_third(self):
        self.assertRaises(ValueError, Drink, "coca",
                          120, -30, -50, "cold soft drink")

        # Check response when arguments values equal to zero are passed to constructor

    def test_init_fourth(self):
        self.assertRaises(ValueError, Drink, "coca",
                          0, 0, 0, "cold soft drink")

        # Check if init works with assert not equal

    def test_fifth(self):
        drink_item = Drink("coca", 120, 30, 50, "cold soft drink")
        self.assertNotEqual(drink_item.price, 50)


if __name__ == "__main__":
    unittest.main()
