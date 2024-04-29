import random
import math

def ValidInput(loopvariable,message,bad_message):
    while True:
        select = CastVariable(message,int)
        if select in loopvariable:
            return select
        else:
            print(bad_message)


def CastVariable(message,type_variable):
    variable = input(message)
    try:
        return type_variable(variable)
    except:
        print("WRONG DATA TYPE")
        return CastVariable(message,type_variable)
     
NumChar = CastVariable("Enter Number Of Characters: ",int)
Characters = []
for i in range(NumChar):
    Name = input("Enter Characters Name: ")
    Strength = math.floor((random.randrange(12) + 1) / (random.randrange(4) + 1)) + 10
    Skill = math.floor((random.randrange(12) + 1) / (random.randrange(4) + 1)) + 10
    Characters.append([Name,Strength,Skill])
    print(Characters)

CSV = open("Characters.csv","w")
for Data in Characters:
    print(Data)
    Charac = ','.join([str(v) for v in Data])
    print(Charac)
    CSV.write(Charac + ",\n")
        