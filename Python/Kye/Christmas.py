Nice = open("Nice.txt","a")
Naughty = open("Naughty.txt","a")
Name = ("Enter Name Of Child: ")
Address = input("Enter Address Of Child: ")
Score = int(input("Enter Score Of Child: "))

if Score > 0:
    Nice.write(f"{Name},{Address}")
else:
    Naughty.write(f"{Name},{Address}")