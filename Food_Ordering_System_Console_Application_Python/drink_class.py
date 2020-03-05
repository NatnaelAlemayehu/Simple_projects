# Author: Natnael Alemayehu

# Importing the item class
from item_class import Item
import main_application
# Dictionary list for the drink item
drink_item = {}


# This is the class drink containing the instance variables and the __init__ method
class Drink(Item):  
    def __init__(self, name, price, volume, stock, description, item_type="drink", item_count_delivered=0,
                 rating=0, review=""):
        if name == "" or price == "" or volume == "" or description == "":
            raise ValueError("Empty value")      
        elif price <= 0 or volume <= 0 or stock <=0:
            raise ValueError("negative or zero value passed")        
        super().__init__(name, price, description, item_type,
                         item_count_delivered, rating, review)
        self.stock = stock
        self.volume = volume          


# This function will display the drink items in the storage
def view_drink_items():
    if drink_item == {}:
        print("currently there are no drink items added")
        main_application.menu()
    else:
        for drink_item_object in drink_item.keys():
            print(drink_item[drink_item_object].name +
                  " ------- RWF {}".format(drink_item[drink_item_object].price))


# Drink1 = Drink("coca",120, -30, -50, "cold soft drink")
