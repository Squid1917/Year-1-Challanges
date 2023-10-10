from ast import *

def Menu(Message, ChoiceA, ChoiceB):
    Choice = input(Message).upper()
    if Choice == ChoiceA.upper():
        return True
    if Choice == ChoiceB.upper():
        return False
    else:
        print("Option not Regognised \nPlease try again")
        Menu(Message, ChoiceA, ChoiceB)

def ReadRecipe():
    RecipeName = input("Enter Recipe Name: ")
    Recipes = open("Recipes.txt", "r").read().split("--")
    Recipe = []
    for i in range(Recipes.__len__()):
        Recipes[i] = Recipes[i].split("\n")
        if (Recipes[i][0] == RecipeName):
            Recipe = Recipes[i]
    if(Recipe == []):
        ReadRecipe()
        return

    IngredientNames = literal_eval(Recipe[1])
    IngredientAmounts = literal_eval(Recipe[2])
    IngredientUnits = literal_eval(Recipe[3])
    print(f"Recipe Name: {Recipe[0]}")
    for i in range(IngredientNames.__len__()):
        print(f"{IngredientAmounts[i]} {IngredientUnits[i]} of {IngredientNames[i]}")

def SaveRecipe():
    RecipeName = input("Enter recipe name: ")
    IngredientNames = []
    IngredientAmounts = []
    IngredientUnits = []
    while True:
        IngredientNames.append(input("Enter Ingredient Name: "))
        IngredientAmounts.append(input("Enter Ingredient Amount: "))
        IngredientUnits.append(input("Enter Ingredient Unit: "))

        if Menu("Would you like to \nA: Add New Ingredient \nB: Exit \n", "A", "B") == False:
            break
    f = open("Recipes.txt","a")
    f.writelines(f"{RecipeName}\n")
    f.writelines(f"{IngredientNames}\n")
    f.writelines(f"{IngredientAmounts}\n")
    f.writelines(f"{IngredientUnits} -- \n")
    f.close()


if (Menu("Would you like to \nA: Read a recipe \nB: Save Recipe \n", "A", "B")):
    ReadRecipe()
else:
    SaveRecipe()
