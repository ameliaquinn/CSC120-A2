import computer

# defines all attributes of the resale shop class 
class ResaleShop:
    inventory: list 

    # constructor 
    def __init__(self):
        self.inventory = []

     # adds a computer to the inventory list 
    def buy(self, c: computer):
        self.inventory.append(c)
    
    # checks to see if a computer is in the inventory, otherwise tells the user the item is not found
    def sell(self, c: computer):
         if c in self.inventory:
              self.inventory.remove(c)
              print("Item " + c + " successfully sold!")
         else: 
              print("Item " +c+ " not found. Please try again!")
    
    # Checks to see that the inventory is non-empty, then prints all items in the inventory
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
     myShop.sell(c)


     
if __name__=="__main__":
    main()