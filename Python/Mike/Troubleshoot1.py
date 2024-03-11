print("Welcome to the troubleshooter!")
print("Please answer questions with either a Y or N")

def CheckInput(Message,AnswerYes):
    answer = input(Message).upper()
    if answer == "Y":
        return not AnswerYes
    elif answer == "N":
        return AnswerYes
    else:
        print("Invalid option")
        return CheckInput(Message,AnswerYes)

while True:
    if CheckInput("Is the phone working as expected: ",True):
        if CheckInput("Is the phone on: ",False):
            if CheckInput("Is the phone charged: ",False):
                if CheckInput("Has the phone been dropped: ",True):
                    if CheckInput("Is the keyboard showing up: ",False):
                        if CheckInput("Is the screen on: ",False):
                            if CheckInput("Has the phone got physicall damage: ",True):
                                if CheckInput("Have you been restarted: ",False):
                                    if CheckInput("Have you cleared the cahce: ",False):
                                        if CheckInput("Have you got free space: ",False):
                                            if CheckInput("Are you connected to the internet: ",False):
                                                print("Welp forward this to higher technitian")
                                            else:
                                                print("Connect to the internet")
                                        else:
                                            print("Clear up some space")
                                    else:
                                        print("Clear the cache")
                                else:
                                    print("Restart")
                            else:
                                print("Contact repairs")
                        else:
                            print("Change the screen")
                    else:
                        print("Get a new phone")
                else:
                    print("Get a new phone")
            else:
                print("Charge the phone up")
        else:                        
            print("Turn the phone on")
    else:
        print("Why are you here")

