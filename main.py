"""
    Filename: main.py
    Description: Main runs the program and is basically just a command list.
    Author & Date: J Gilleman & Ryan (K) Emerson September 18, 2022
"""

# Import; letting this file call other files
from computer import Computer
from oo_resale_shop import ResaleShop

# """ This helper function takes in a bunch of information about a computer,
#     and packages it up into a python dictionary to make it easier to store

#     Note: because python is dynamically typed, you may not be used to seeing 
#     explicit data types (str, int, etc.) listed in a python function. We're 
#     going to go the extra step, because when we get to Java it'll be required!""""

# def create_computer(description: str,
#                     processor_type: str,
#                     hard_drive_capacity: int,
#                     memory: int,
#                     operating_system: str,
#                     year_made: int,
#                     price: int):
#     return {'description': description,
#             'processor_type': processor_type,
#             'hard_drive_capacity': hard_drive_capacity,
#             'memory': memory,
#             'operating_system': operating_system,
#             'year_made': year_made,
#             'price': price
#     }"""

def main():
    
    shop = ResaleShop()

    # Variable; "computer()" calls the constuctor in the computer class, which makes a new computer for me
    computer = Computer(
        "Mac Pro (Late 2013)",              # name
        "3.5 GHc 6-Core Intel Xeon E5",     # cpu
        1024,                               # hd
        64,                                 # ram
        "macOS Big Sur",                    # os
        2013,                               # year
        1500                                # price
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer.description)
    print("Adding to inventory...")
    computer_id = shop.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    #Update price of our one computer
    print("Updating price to be 100$ more. The previous price was", shop.inventory[computer_id].price)
    shop.update_price(computer_id, 1600)
    print("The price for that computer is now", shop.inventory[computer_id].price, " \n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
