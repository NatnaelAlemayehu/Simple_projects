# Author: Natnael Alemayehu

# This file contains the test for the drink class

import unittest
import admin_user


# Class testing case
class TestCaseMethod(unittest.TestCase):
    def test_init(self):
        # Testing when empty arguments are passed to food item adding function
        self.assertRaises(ValueError, admin_user.add_food_item,
                          "", "", "", "")

    def test_init_second(self):
        # Testing when empty arguments are passed to drink item adding function
        self.assertRaises(ValueError, admin_user.add_drink_item,
                          "", "", "", "", "")

        # Testing when empty arguments are passed to food item removing function

    def test_init_third(self):
        self.assertRaises(ValueError, admin_user.remove_food_item, "")

        # Testing when empty arguments are passed to drink item removing function

    def test_init_fourth(self):
        self.assertRaises(ValueError, admin_user.remove_drink_item, "")

        # Testing when empty arguments are passed to drink item updating function

    def test_fifth(self):
        self.assertRaises(ValueError, admin_user.update_drink_information, "", "")


if __name__ == "__main__":
    unittest.main()
