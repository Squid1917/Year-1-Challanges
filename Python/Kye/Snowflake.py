import turtle

elsa = turtle.Turtle()
turtle.Screen().bgcolor("white")
colors = ["cyan", "purple", "white", "blue", "red", "lime"]


elsa.penup()
elsa.fd(90)
elsa.lt(45)
elsa.pendown()
elsa.speed(50)

def branch():
    for i in range(3):
        for i in range(3):
            elsa.fd(30)
            elsa.bk(30)
            elsa.rt(45)
        elsa.lt(90)
        elsa.bk(30)
        elsa.lt(45)
    elsa.rt(90)
    elsa.fd(90)

def snowflake():
    elsa.clear()
    for i in range(8):
        branch()
        elsa.left(45)

while True:
    snowflake()