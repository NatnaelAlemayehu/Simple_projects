# Author: Mahalinoro Razafimanjato

# This file contains the test for the user class

import unittest
from user_class import User


# Class testing case
class TestCaseMethod(unittest.TestCase):
    def test_init(self):
        # Testing if init method is working
        user_one = User('Naomi')
        self.assertEqual(user_one.name, 'Naomi')

    def test_init_second(self):
        # Testing if init method is working
        user_two = User('Tahiry')
        self.assertNotEqual(user_two.name,'Naomi')

    def test_view_account_info(self):
        # Testing if view account info is displaying the correct output
        user_one = User('Naomi')
        self.assertEqual(user_one.view_account_info(), 'Naomi')

    def test_view_account_info_second(self):
        # Testing if the view account info function is displaying the correct output
        user_two = User('Tahiry')
        self.assertNotEqual(user_two.view_account_info(), 'Naomi')

    def test_init_third(self):
        # Testing if the value in name is an empty string
        self.assertRaises(ValueError, User, "")


if __name__ == "__main__":
    unittest.main()
