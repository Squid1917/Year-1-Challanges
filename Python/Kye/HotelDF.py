import pandas as pd

def GetRooms():
    DF = pd.read_csv(open("Hotel.csv","r"))
    return DF

    # print(DF.to_string(index=False))


def ValidInput(loopvariable,message,bad_message):
    for i, item in enumerate(loopvariable, 1):
        print(i, item)
    sel_check = False
    while not sel_check:
        select = CastVariable(message,int) #Cast as an int
        if select > 0 and select < len(loopvariable) + 1:
            sel_check = True
            return select
        else:
            print(bad_message)

def CastVariable(message,type_variable):
    variable = input(message)
    try:
        return type_variable(variable)
    except:
        print("WRONG DATA TYPE")
        return CastVariable(message,type_variable)

def SaveRooms(Rooms):
    CSV = open("Hotel.csv","w")
    for Room in Rooms:
        Room_Data = ','.join([str(v) for v in Room])
        CSV.write(Room_Data + ",\n")

def PrintRooms(Rooms):
    for Room in Rooms:
        PrintRoom(Room)

def ViewRoom(Rooms):
    ID_Lookup = CastVariable("Enter Room ID: ",int)
    row_index = Rooms.query('`Room ID` == @ID_Lookup').index[0]
    Room = Rooms.iloc[[row_index]]
    print(Room)

def PrintRoom(Room):
    print(Room)
    
        
def ViewBookings(Rooms):
    for index, Room in Rooms.iterrows():
        
        if(Room['Occupier'] != "Empty"):
            print(Room[3])
            print(f"{Room[3]} has booked room ID of {Room[0]} which has {Room[4]} beds and is a {Room[1]} rated room")

def AddBooking(Rooms):
    Beds = CastVariable("How many Beds: ",int)
    Price = CastVariable("Enter max price (Min of 100): ",int)
    TypeIndex = ValidInput(["Basic","Advanced","Premium"],"Enter room type: ","Not a room type")
    Type = ["Basic","Advanced","Premium"][TypeIndex - 1]
    print(Type)
    PotRooms = []
    for index, Room in Rooms.iterrows():
        if Room['Occupier'] == "Empty" and Room['Beds'] == Beds and Room['Cost'] <= Price and Room['Type'] == Type:
            PotRooms.append(Room)
    PrintRooms(PotRooms)


def AddRoom(Rooms):
    RoomType = ["Basic","Advanced","Premium"]
    ID = Rooms['Room ID'].max() + 1
    Type = RoomType[ValidInput(["Basic","Advanced","Premium"],"Enter room type: ","Not a room type")]
    Cost = CastVariable("Enter Cost",int)
    Occupier = "Empty"
    Beds = CastVariable("Enter Bed Count",int)
    Persons = CastVariable("Enter Max Persons",int)
    Room = [ID,Type,Cost,Occupier,Beds,Persons]
    Rooms.append(Room)
    SaveRooms(Rooms)

def Menu():
    Rooms = GetRooms()
    while True:
        Selection = CastVariable("Select Option \n\n"
            "1. View Room \n"
            "2. View Bookings \n"
            "3. Book Room \n"
            "4. Add Room \n"
            "5. Print Rooms \n"
            "6. Exit \n",int
            )
        if Selection == 1:
            PrintRoom(ViewRoom(Rooms))
        elif Selection == 2:
            ViewBookings(Rooms)
        elif Selection == 3:
            AddBooking(Rooms)
        elif Selection == 4:
            AddRoom(Rooms)
        elif Selection == 5:
            PrintRooms(Rooms)
        elif Selection == 6:
            exit()

Menu()
# GetRooms()