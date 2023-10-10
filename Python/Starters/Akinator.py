def CheckInput(Message):
    Choice = input(Message).upper()
    if Choice == "Y":
        return True
    if Choice == "N":
        return False
    else:
        print("Please try again")
        CheckInput(Message)


print("Select: Harry Potter, Ninblago, The Martian, Star Wars, Baby Driver, Ready Player One")
if CheckInput("Is the film Futuristic Y/N: "):
    if CheckInput("Is the film magical Y/N: "):
        print("It is Harry Potter EWWWW")
    else:
        print("It is Ninblago")
else:
    if CheckInput("Does it have cars Y/N: "):
        if CheckInput("Does it have MATT THE DAMON: "):
            print("It is the Martian")
        else:
            print("It is Star Wars")
    else:
        if CheckInput("Does it have a giant EGG: "):
            print("It is Ready Player One")
        else:
            print("It is Baby Driver")
