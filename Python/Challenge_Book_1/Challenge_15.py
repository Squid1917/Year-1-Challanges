password = "changeme"
tries = 0

while True:
    guess = input("Enter password")

    if guess != password:
        print("Incorrect")
        tries += 1
    
    elif guess == password:
        print(f"Accepted in {tries} tries")
        break

    if(tries >= 5):
        input("Access denied, please press enter to exit  and contact security to reset your password")
        break