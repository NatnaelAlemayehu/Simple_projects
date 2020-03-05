# Author: Natnael Alemayehu

# Importing Item class
from item_class import Item
import main_application
# Dictionary list containing the food item
food_item = {}


# This is the class for Food, child of Item
# Containing the instance variables and the __init__ method to instantiate automatically
class Food(Item):
    def __init__(self, name, price, size, description, item_type="food", item_count_delivered=0,
                 rating=0, review=""):
        if name == "" or price == "" or size == "" or description == "":            
            raise ValueError("Empty value")
        elif price <= 0:
            raise ValueError("negative or zero value passed")
        elif price >= 100000:
            raise ValueError("unrealistic price passed")
        super().__init__(name, price, description, item_type,
                         item_count_delivered, rating, review)
        self.size = size
    

# This function will display the list of food items in the storage
def view_food_items():
    if food_item == {}:
        print ("currently there are no food items added") 
        main_application.menu()       
    else:
        for food_item_object in food_item.keys():
            print(food_item[food_item_object].name + " ------- RWF {}".format(food_item[food_item_object].price))
