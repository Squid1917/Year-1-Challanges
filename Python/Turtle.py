from turtle import *

size = 100
sides = int(input("HEY BOZO INPUT NUMBER OF SIDES: "))
angle = 360/sides

Bob = Turtle()
Bob.hideturtle()
Bob.begin_fill()
Bob.color("Red")

for i in range(sides):
    Bob.forward(size)
    Bob.right(angle)

Bob.end_fill()
done()