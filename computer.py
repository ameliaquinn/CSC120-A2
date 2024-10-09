from typing import Optional

# define all attributes of the Computer class
class Computer:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int



    # constructor
    def __init__(self, description, processor_type,hard_drive_capacity,memory,operating_system,year_made,price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # sets price to user's input
    def update_price(self,new_price: int):
        self.price = new_price
    
    # checks the year made, sets new price, also updates operating system
    def refurbish(self, new_os: Optional[str]=None):
        if self.year_made < 2000:
            self.price = 0
        elif self.year_made < 2012:
            self.price = 250
        elif self.year_made < 2018:
            self.price = 550
        else:
            self.price = 1000
        if new_os is not None:
            self.operating_system = new_os

    # prints all details about the computer
    def printDetails(self):
        print("Description: " + self.description)
        print("Processor type: " + self.processor_type)
        print("Hard drive capacity: " + self.hard_drive_capacity)
        print("Memory: "+self.memory)
        print("Operating system: "+self.operating_system)
        print("Year made: "+self.year_made)
        print("Price: "+self.price)