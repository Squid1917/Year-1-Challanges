Items = ["Coffee","Tea","Muffin","Smoothie","Toast"] #? Define Items
Prices = {"Coffee": 2.50, "Tea": 1.50, "Muffin" : 2.00, "Smoothie": 3.00, "Toast": 5} #? Define the item prices in a dictionary
CurrentItems = []  #? Define basket
TotalPrice = 0.00  #? Define total price

print(f"Welcome to the cafe we have {Items}")  #? Print out all the items
print("Type 'Exit' after last item")

while True: #? Loop forever
    Item = input("Enter item to order: ") #? Input the item
    if Item.capitalize() in Items: #? Is Item A Valid Item
        CurrentItems.append(Item) #? Add item to basket
        TotalPrice += Prices[Item] #? Total the final price
        print(f"{Item} is £{Prices[Item]}")  #? Print Receipt
    elif Item.lower() == "exit":  #? Exit if last item
        break #? Exit the loop
    else:
        print(f"'{Item}' is not a valid item") #? Print Not Valid Item

print(f"Total: £{TotalPrice}")  #? Output total price