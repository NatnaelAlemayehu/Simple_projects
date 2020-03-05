from food_class import Food
import unittest


# Author: Natnael Alemayehu

# This file contains the test for the drink class


# Class testing case

class TestCaseMethod(unittest.TestCase):
    def test_init(self):
        # Testing if init method is working
        food_item = Food("cheese burger", 120, "Large", "delicious")
        self.assertEqual(food_item.name, 'cheese burger')
        
        # when empty arguments are passed to constructor
    def test_init_second(self):
        self.assertRaises(ValueError, Food, "",
                          "", "", "", "", "", "")

        # Testing when negative argument values are passed to constructor for some arguments
    def test_init_third(self):
        self.assertRaises(ValueError, Food, "cheese burger", -120, "Large",
                          "delicious")

        # Check response when arguments values equal to zero are passed to constructor
    def test_init_fourth(self):
        self.assertRaises(ValueError, Food, "cheese burger", 0, "Large",
                          "delicious")

        # Check response when big values are passed for price
    def test_fifth(self):
        self.assertRaises(ValueError, Food, "cheese burger", 12454534540, "Large",
                          "delicious")


if __name__ == "__main__":
    unittest.main()
