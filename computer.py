"""
    Filename: computer.py
    Description: Computer holds all the information about the computer like processor and os type. It also creates a computer object when called.
    Author & Date: J Gilleman & Ryan (K) Emerson September 18, 2022
"""
class Computer:

    #I defined my attributes in my constructor
    
    # Constuctor; make computer and have it hold all this information about itself
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # I've set up my program so that Computer just holds information and doesn't control anything. So I have no methods for this class.
