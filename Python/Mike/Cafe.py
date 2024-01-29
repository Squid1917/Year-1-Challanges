Items = ["Coffee","Tea","Muffin","Smoothie","Toast"]
Prices = {"Coffee": 2.50, "Tea": 1.50, "Muffin" : 2.00, "Smoothie": 3.00, "Toast": 5}
CurrentItems = []
TotalPrice = 0.00

print("Welcome to the cafe we have " , Items)

print("Type 'Exit' after last item")
while True:
    Item = input("Enter item to add: ")
    if Item in Items:
        CurrentItems.append(Item)
    elif Item == "Exit":
        break 
    else:
        print("Error: Item not in database")

for Item in CurrentItems: 
    TotalPrice += Prices[Item]
    print(f"{Item} is {Prices[Item]}")

print(f"Total: {TotalPrice}")