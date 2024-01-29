Items = ["Coffee","Tea","Muffin","Smoothie","Toast"] #? Define Items
Prices = {"Coffee": 2.50, "Tea": 1.50, "Muffin" : 2.00, "Smoothie": 3.00, "Toast": 5} #? Define the item prices in a dict
CurrentItems = []  #? Define basket
TotalPrice = 0.00  #? Define total price

print("Welcome to the cafe we have " , Items)  #? Print out all the items
print("Type 'Exit' after last item")

while True: #? Loop forever
    Item = input("Enter item to add: ") #? Input the item
    if Item in Items: #? Check if valid
        CurrentItems.append(Item) #? Add item to basket
    elif Item == "Exit":  #? Exit if last item
        break  
    else:
        print("Error: Item not in database") #? Error Handleing

for Item in CurrentItems:  #? Loop over basket
    TotalPrice += Prices[Item] #? Total the final price