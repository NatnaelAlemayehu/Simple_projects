# Author: Natnael Alemayehu

# import food_class
# import drink_class
# importing time
import time

# List containing the different places for delivery
fast_time_delivery_places = ["remera", "gishushu", "town", "downtown", "nyarutarama""nyarugenge" ]
medium_time_delivery_places = ["nyamirambo", "butamwa", "gisozi", "kacyiru", "kanombe", "kicukiro", "gikondo"]


# This is the parent class Item
class Item:
    # The __init__ method to instantiate a new object automatically
    def __init__(self, name, price, description, item_type, item_count_delivered, rating, review):
        if name == "" or price == "" or description == "" or item_type == "": 
            raise ValueError("Empty value")        
        elif price <= 0 or rating < 0:
            raise ValueError("negative or zero value passed")
        elif price >= 100000 or rating > 5:
            raise ValueError("unrealisitic price passed")
        self.name = name
        self.price = price
        self.item_type = item_type
        self.item = description
        self.item_count_delivered = item_count_delivered
        self.rating = rating
        self.review = review
    
    def user_rating(self, user_rating_value):
        # Method to update value for the variable rating
        self.rating = user_rating_value
    
    def user_reviewing(self, user_review):
        # Method to update value in variable review
        self.review = user_review
    
    def calculate_total_price(self, user_choice_item, amount, itemtype):
        # Method to calculate the price for drink or food
        import food_class
        import drink_class
        if itemtype == "food":
            if user_choice_item in food_class.food_item.keys():
                calculated_price = self.price * amount
                return calculated_price
        elif itemtype == "drink":
            if user_choice_item in drink_class.drink_item.keys():
                calculated_price = self.price * amount
                return calculated_price


# Function that display if the food/drink has been delivered or not depending on the user's location
# Time will displayed based on the location [is it far or not]
def delivery(user_location):
    if type(user_location) == int:
        raise ValueError("non string type passed")
    if user_location in fast_time_delivery_places:
        print("item will be delivered in 20-30 minutes")
        time.sleep(3)
        print("item delivered")
    elif user_location in medium_time_delivery_places:
        print("item will be delivered in 30-40 minutes")
        time.sleep(4)
        print("item delivered")
    

