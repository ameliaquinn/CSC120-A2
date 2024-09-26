from typing import Optional
class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int



    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type,hard_drive_capacity,memory,operating_system,year_made,price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def update_price(self,new_price: int):
        self.price = new_price
    
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
