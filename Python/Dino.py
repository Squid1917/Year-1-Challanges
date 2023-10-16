import time
def CheckInput(Message):
    Choice = input(Message).upper()
    if Choice == "Y":
        return True
    if Choice == "N":
        return False
    else:
        print("Please try again")
        CheckInput(Message)

Dino = ["Triceratops","Stegosaurus","Trex","Nigersaurous","Pterodactyl","Diplodocus"]
def Program():
    print("Select: Triceratops,Stegosaurus,Trex,Nigersaurous,Pterodactyl,Diplodocus")
    if CheckInput("Has Three Horns Y/N: "):
        print(f"Your Dino is {Dino[0]}")
    else:
        if CheckInput("Has Spikes On Back Y/N: "):
            print(f"Your Dino is {Dino[1]}")
        else:
            if CheckInput("Has Tiny Hands Y/N: "):
                print(f"Your Dino is {Dino[2]}")
            else:
                if CheckInput("Looks Like Lewis Y/N: "):
                    print(f"Your Dino is {Dino[3]}")
                else:
                    if CheckInput("Can It Fly Y/N: "):
                        print(f"Your Dino is {Dino[4]}")
                    else:
                        if CheckInput("Is It an Ali-A meme Y/N: "):
                            print(f"Your Dino is {Dino[5]}")
                        else:
                            print("Your Dino Is Spinosaurus")


while True:
    Program()
    print("Resetting Please Wait")
    time.sleep(5)
    print("Next User Please")