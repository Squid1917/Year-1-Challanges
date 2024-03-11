def Get_Data():
    CSV = open("Football.csv","r")
    Data = []
    for Line in CSV:
        TempData = (Line.split(","))
        del TempData[-1]
        Data.append(TempData)
    return Data

def SaveData(BigData):
    CSV = open("Football.csv","w")
    for Data in BigData:
        Team_Data = ','.join([str(v) for v in Data])
        CSV.write(Team_Data + ",\n")

def Add_Team(Data):
    Position = int(input("Enter Team Position: "))
    TeamName = input("Enter Team Name: ")
    Points = int(input("Enter Points: "))
    Wins = int(input("Enter Wins: "))
    Draws = int(input("Enter Draws: "))
    Losses = int(input("Enter Losses: "))
    TeamData = [Position,TeamName,Points,Wins,Draws,Losses]
    Data.append(TeamData)
    SaveData(Data)

def Edit_Team(Data):
    Name = input("Enter Team Name To Search: ")
    for i in range(Data.__len__()):
        if Data[i][1] == Name:
            Team = Data[i]
            print(Team)
    
    EditData = input("Enter Field To Edit: ")
    
    if EditData == "Position":
        ChangedData = input("Enter Correct Data for Position: ")
        Team[0] = ChangedData
    elif EditData == "Name":
        ChangedData = input("Enter Correct Data for Name: ")
        Team[1] = ChangedData
    elif EditData == "Points":
        ChangedData = input("Enter Correct Data for Points: ")
        Team[2] = ChangedData
    elif EditData == "Wins":
        ChangedData = input("Enter Correct Data for Wins: ")
        Team[3] = ChangedData
    elif EditData == "Draws":
        ChangedData = input("Enter Correct Data for Draws: ")
        Team[4] = ChangedData
    elif EditData == "Losses":
        ChangedData = input("Enter Correct Data for Losses: ")
        Team[5] = ChangedData
    
    SaveData(Data)
    
def Locate_Team(Data):
    Name = input("Enter Team Name")
    for i in range(0,Data.__len__()):
        if Data[i][1] == Name:
            Team = Data[i]
    print("Position: {}, Team Name: {}, Points: {}, Wins: {}, Draws: {}, Losses: {}".format(*Team))

def Remove_Team(Data):
    Name = input("Enter Team Name To Remove: ")
    for i in range(0,Data.__len__()):
        if Data[i][1] == Name:
            del Data[i]
            break
    SaveData(Data)

Data = Get_Data()
while True:
    Selection = int(input("""Enter Selection
    1) Add Team
    2) Edit Team
    3) Locate Team
    4) Remove Team
    5) Exit
    """))
    
    if Selection == 1:
        Add_Team(Data)
    elif Selection == 2:
        Edit_Team(Data)
    elif Selection == 3:
        Locate_Team(Data)
    elif Selection == 4:
        Remove_Team(Data)
    elif Selection == 5:
        exit()
    else:
        print("Invalid Option")