Names = []
Grades = []
Scores = []
Dates = []
Papers = []
Tutors = []

FileName = "Grades.csv"

def TryQuit(Message):
    Choice = input(Message).upper()
    if Choice == "Y".upper():
        return True
    if Choice == "N".upper():
        return False
    else:
        print("Option not Regognised \nPlease try again")
        TryQuit(Message)

def AddGrade():
    while True:
        Name = (input("Enter name of student: "))
        Names.append(Name)
        Scores.append(int(input(f"Enter score of {Name}: ")))
        Dates.append(input(f"Enter the date that {Name} did the paper: "))
        Papers.append(input(f"Enter the paper {Name} did: "))
        Tutors.append(input(f"Enter tutor that marked the paper: "))
        
        if TryQuit("Would you like to exit Y/N: "):
            break

    for i in range(Scores.__len__()):
        if Scores[i] > 80:
            Grades.append("A*")
        elif Scores[i] > 70:
            Grades.append("A")
        elif Scores[i] > 60:
            Grades.append("B")
        elif Scores[i] > 50:
            Grades.append("C")
        elif Scores[i] > 40:
            Grades.append("D")
        else:
            Grades.append("FAIL")
    File = open(FileName,"a")

    for i in range(Names.__len__()):
        File.write(f"{Names[i]},{Grades[i]},{Papers[i]},{Dates[i]},{Tutors[i]},\n")
        print(f"{Names[i]}'s grade is {Grades[i]}")

    File.close()

def ViewGrades():
    File = open(FileName,"r")

    for line in File.readlines():
        line = line.split(",")
        Names.append(line[0])
        Grades.append(line[1])
        Papers.append(line[2])
        Dates.append(line[3])
        Tutors.append(line[4])

    for i in range(Names.__len__()):
        print(f"{Names[i]}'s grade is {Grades[i]} on the paper {Papers[i]} on the {Dates[i]} marked by {Tutors[i]}")

    File.close()

def Menu():
    Choice = input("Would you like to \nA: Add Grade \nB: View Grades \nC: Exit \n").upper()
    if Choice == "A":
        AddGrade()
    elif Choice == "B":
        ViewGrades()
    else:
        exit()

Menu()