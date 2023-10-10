from random import *
ran_num = random.randint(0,100)
counter = 0

while True:
    guess = int(input("Enter number: "))

    if ran_num == guess:
        print("Correct")
        break

    if guess > ran_num:
        print("Lower")
    if guess < ran_num:
        print("Higher")
    counter += 1