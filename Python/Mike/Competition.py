import re as regex

def CheckInput(Message):
    Choice = input(Message).upper()
    if Choice == "A":
        return "Chess"
    if Choice == "B":
        return "Billiads"
    if Choice == "C":
        return "Darts"
    else:
        print("Please try again")
        return CheckInput(Message)

def CheckName(Message):
    Choice = input(Message).upper()
    if regex.search(r'^(?=.*[A-Z])(?=.*\d).{1,}$', Choice):
        return Choice
    else:
        print("Please try again")
        return CheckInput(Message)

Username = CheckName("Enter Username Must Contain 1 Capital And Number:")
Competition = CheckInput("Enter Competition \nA) Chess\nB) Billiads \nC) Darts \n")

print(f"{Username} has entered the competition {Competition}")