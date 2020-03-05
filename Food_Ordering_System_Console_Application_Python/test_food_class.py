# Author: Natnael Alemayehu

# This file contains the test for the drink class

import unittest
from food_class import Food


# Class testing case
class TestCaseMethod(unittest.TestCase):
    def test_init(self):
        # Testing if init method is working
        food_item = Food("cheese burger", 120, "Large", "fresh burger")
        self.assertEqual(food_item.name, 'cheese burger')

    def test_init_second(self):
        # when empty arguments are passed to constructor
        self.assertRaises(ValueError, Food, "",
                          "", "", "")

        # Testing when negative argument values are passed to constructor for some arguments

    def test_init_third(self):
        self.assertRaises(ValueError, Food, "cheese burger",
                          43444353453, "Large", "fresh burger")

        # Check response when arguments values equal to zero are passed to constructor

    def test_init_fourth(self):
        self.assertRaises(ValueError, Food, "cheese burger",
                          0, "Large", "fresh burger")

        # Check response if the init method is working using assert not equal

    def test_fifth(self):
        food_item = Food("cheese burger", 20, "Large", "fresh burger")
        self.assertNotEqual(food_item.price, 50)


if __name__ == "__main__":
    unittest.main()
