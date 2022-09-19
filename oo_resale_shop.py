"""
    Filename: oo_resale_shop.py
    Description: The resale shop handles all buying, selling, price updating, and inventory printing for this program. 
                It also generates the inventory once main first call the resale shop.
    Author: J Gilleman & Ryan (K) Emerson
    Date: September 18, 2022
    Cited: I did not utilize any external resources in completing this assignment.
"""
from computer import Computer
from typing import Dict, Union, Optional
class ResaleShop:

    # Attributes: I don't have any listed here because I've made it so my attributes (inventory and itemID) get creating in the constructor

    # Constructor, sets up the shop inventory when resale shop is created
    def __init__(self):
        self.inventory : Dict[int, Computer] = {}
        self.itemID = 0

    # Takes in a Dict containing all the information about a computer,
    # adds it to the inventory, returns the assigned item_id
    def buy(self, computer: Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID
    
    # Takes in an item_id and a new price, updates the price of the associated
    # computer if it is the inventory, prints error message otherwise
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price    #inventory[itemID] is a computer
        else:
            print("Item", item_id, "not found. Cannot update price.")

    # Takes in an item_id, removes the associated computer if it is the inventory, 
    # prints error message otherwise
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    #prints all the items in the inventory (if it isn't empty), prints error otherwise
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    #refurbish computer by updating os if it's super old, and updating the price as well
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")