import random

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
     
while True:
    DiceNum = ValidInput([4,6,12],"Enter Faces Of Dice 4,6,12: ","Not an option")
    Roll = random.randrange(DiceNum) + 1
    print(f"{DiceNum} sided dice thrown, score {Roll}")