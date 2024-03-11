def GetRooms():
    CSV = open("Hotel.csv","r")
    Data = []
    for Line in CSV:
        TempData = (Line.split(","))
        del TempData[-1]
        Data.append(TempData)
    return Data

def valid_input(loopvariable,message,bad_message):
    for i, item in enumerate(loopvariable, 1):
        print(i, item)
        
    sel_check = False
    while not sel_check:
        select = cast_variable(message,int) #Cast as an int
        if select > 0 and select < len(loopvariable) + 1:
            sel_check = True
            return select
        else:
            print(bad_message)

def cast_variable(message,type_variable):
    variable = input(message)
    try:
        return type_variable(variable)
    except:
        print("WRONG DATA TYPE")
        return cast_variable(message,type_variable)

def SaveRooms(Rooms):
    CSV = open("Hotel.csv","w")
    for Room in Rooms:
        Room_Data = ','.join([str(v) for v in Room])
        CSV.write(Room_Data + ",\n")

def PrintRooms(Rooms):
    for Room in Rooms:
        PrintRoom(Room)

def PrintRoom(Room):
    if Room:
        print("ID: {}, Type: {}, Cost: {}, Occupier: {}, Beds: {}, Persons: {}".format(*Room))

def ViewRoom(Rooms,ID_Lookup):
    for Room in Rooms:
        if  Room[0] == ID_Lookup:
            return Room
        
def ViewBookings(Rooms):
    for Room in Rooms:
        if(Room[3] != "Empty"):
            print(f"{Room[3]} has booked room ID of {Room[0]} which has {Room[4]} beds and is a {Room[1]} rated room")

def AddBooking(Rooms):
    Beds = cast_variable("How many Beds: ",int)
    Price = cast_variable("Enter max price (Min of 100): ",int)
    Type = valid_input(["Basic","Advanced","Premium"],"Enter room type: ","Not a room type")
    PotRooms = []
    for Room in Rooms:
        if Room[3] == "Empty" and Room[4] == Beds and int(Room[2]) < Price and Room[1] == Type:
            print(f"Room Found ID of {Room[0]}")
            PotRooms.append(Room)
    print(PotRooms)

def AddRoom(Rooms):
    RoomType = ["Basic","Advanced","Premium"]
    ID = cast_variable("Enter ID: ",int)
    Type = RoomType[valid_input(["Basic","Advanced","Premium"],"Enter room type: ","Not a room type")]
    Cost = cast_variable("Enter Cost",int)
    Occupier = "Empty"
    Beds = cast_variable("Enter Bed Count",int)
    Persons = cast_variable("Enter Max Persons",int)
    Room = [ID,Type,Cost,Occupier,Beds,Persons]
    Rooms.append(Room)
    SaveRooms(Rooms)


def Menu():
    Rooms = GetRooms()
    while True:
        Selection = cast_variable("Select Option \n\n"
            "1. View Room \n"
            "2. View Bookings \n"
            "3. Book Room \n"
            "4. Add Room \n"
            "5. Print Rooms \n"
            "6. Exit \n",int
            )
        if Selection == 1:
            PrintRoom(ViewRoom(Rooms,input("Enter Room ID: ")))
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