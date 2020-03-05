# Author: Mahalinoro Razafimanjato

# This file contains the test for regular user class

# Import unittest for unit testing
import unittest
from regular_user_class import *


# Class for the testing cases
class TestCaseMethods(unittest.TestCase):
    def test_init(self):
        # Testing the init method if it works
        regular_user_one = RegularUser('Mahaly', 'Kacyiru', 300)
        self.assertEqual(regular_user_one.name, 'Mahaly')
        self.assertEqual(regular_user_one.location, 'Kacyiru')
        self.assertNotEqual(regular_user_one.wallet, 20)

    def test_update_information(self):
        # Testing the update information method if it update the instance variables
        regular_user_one = RegularUser('Mahaly', 'Kacyiru', 300)
        self.assertEqual(regular_user_one.update_information('Hello', 'Kigali'), ('Hello', 'Kigali'))

    def test_add_money(self):
        # Testing the add money method if it gives correct answer
        regular_user_one = RegularUser('Mahaly', 'Kacyiru', 300)
        self.assertEqual(regular_user_one.add_money(20), 320)

    def test_add_not_money(self):
        regular_user_one = RegularUser('Mahaly', 'Kacyiru', 20)
        self.assertNotEqual(regular_user_one.add_money(2), 10)

    def test_subtract_money(self):
        # Testing the subtract money method if it gives correct answer
        regular_user_one = RegularUser('Mahaly', 'Kacyiru', 20)
        self.assertEqual(regular_user_one.subtract_money(15), 5)

    def test_subtract_not_money(self):
        regular_user_one = RegularUser('Mahaly', 'Kacyiru', 20)
        self.assertNotEqual(regular_user_one.subtract_money(2), 52)

if __name__ == "__main__":
    unittest.main()
