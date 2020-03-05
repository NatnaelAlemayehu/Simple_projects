# Author: Mahalinoro Razafimanjato


# This is the class user parent for every kind of user
class User:
    # Method __init__ to instantiate the user automatically
    def __init__(self, name):
        self.name = name
        if name == "":
            raise ValueError("Empty value")

    def __str__(self):
        pass

    # Method to view the name information of the specific instance
    def view_account_info(self):
        return self.name
