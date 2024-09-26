class ResaleShop:

    # What attributes will it need?
    inventory: list 

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    # GOAL: add c to self.inventory
    def buy(self, c: str):
            self.inventory.append(c)
    
    def sell(self, itemID: int):
         if itemID < len(self.inventory):
              del self.inventory[itemID]
              print("Item", itemID, "successfully sold!")
         else: 
              print("Item", itemID, "not found. Please try again!")
    def print_inventory(self):
         if self.inventory:
              for i in self.inventory:
                  print("Item ID:", i) 
                  print("Name:", self.inventory[i])
              else: 
                   print("No inventory to display!")
              
            
              

         

def main():
     myShop: ResaleShop = ResaleShop()
     print("There are", len(myShop.inventory), "items in stock.")
     c = "My Awesome Computer"
     myShop.buy(c)
     print("There are now", len(myShop.inventory), "items in stock.")
     myShop.sell(1)


     
if __name__=="__main__":
    main()