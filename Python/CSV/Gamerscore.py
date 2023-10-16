File = open("gamescore.csv","r")
Line = File.readline()
SearchName = input("Enter name to search: ")
Found = False

while (Line):
    Data = Line.split(",")
    if int(Data[1]) < 6000:
        print(f"Handle: {Data[0]}")
    Line = File.readline()
