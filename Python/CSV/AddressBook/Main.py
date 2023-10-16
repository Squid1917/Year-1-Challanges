File = open("Addresses.csv", "r")
line = File.readline()
UserSearch = input("What would you like to search: ")
Found = False


for line in File:
    Data = line.split(",")
    if UserSearch in Data:
        Found = True
        print(line)

if Found == False:
    Add = input("That user is not in our database would you like to add a new contact Y/N: ")
    if Add == "Y":
        Forename = input("Please enter the Forename: ")
        Surname = input(f"Please enter {Forename}'s Surname: ")
        Address = input(f"Please enter {Forename}'s Address: ")
        City = input(f"Please enter {Forename}'s City: ")
        Number = input(f"Please enter {Forename}'s Number: ")
        File = open("Addresses.csv", "a")
        FinalData = Forename + "," + Surname + "," + Address + "," + City + "," + Number
        File.write(FinalData)
