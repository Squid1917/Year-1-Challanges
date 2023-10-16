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
    NewServingSize = int(input("Enter Serving Size: "))
    Recipes = open("Python\Recipes.txt", "r").read().split("--")
    Recipe = []
    for i in range(Recipes.__len__()):
        Recipes[i] = Recipes[i].split("\n")
        if (Recipes[i][0] == RecipeName):
            Recipe = Recipes[i]
    if(Recipe == []):
        ReadRecipe()
        return
    
    IngredientNames = literal_eval(Recipe[1])
    IngredientAmounts = list(map(int,literal_eval(Recipe[2])))
    IngredientUnits = literal_eval(Recipe[3])
    ServingSize = int(Recipe[4])
    print(f"For a {RecipeName} for {NewServingSize} people you will need:")
    
    for i in range(IngredientAmounts.__len__()):
        IngredientAmounts[i] = IngredientAmounts[i] / ServingSize * NewServingSize
        print(f"{IngredientAmounts[i]} {IngredientUnits[i]} of {IngredientNames[i]}")



def SaveRecipe():
    RecipeName = input("Enter recipe name: ")
    ServingSize = int(input("Enter Serving Size: "))
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
    f.writelines(f"{IngredientUnits}\n")
    f.write(f"{ServingSize} -- \n")
    f.close()


if (Menu("Would you like to \nA: Read a recipe \nB: Save Recipe \n", "A", "B")):
    ReadRecipe()
else:
    SaveRecipe()
