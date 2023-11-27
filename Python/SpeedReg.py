Iterations = int(input("Enter number of vehicles to test: "))

NonStandard = 0
Regs = []

for i in range(Iterations):
    Reg = input("Enter Reg: ") # Determain how many times to loop over
    if Reg.__len__() == 8:
        if Reg[0].isalpha():
            if Reg[1].isalpha():
                if Reg[2].isnumeric():
                    if Reg[3].isnumeric():
                        if Reg[4] == " ":
                            if Reg[5].isalpha():
                                if Reg[6].isalpha():
                                    if Reg[7].isalpha(): 
                                        NonStandard += 0
                                        print("Legal")
                                    else:
                                        NonStandard += 1
                                        Regs.append(Reg)
                                else:
                                    NonStandard += 1
                                    Regs.append(Reg)
                            else:
                                NonStandard += 1
                                Regs.append(Reg)
                        else:
                            NonStandard += 1
                            Regs.append(Reg)
                    else:
                        NonStandard += 1
                        Regs.append(Reg)
                else:
                    NonStandard += 1
                    Regs.append(Reg)
            else:
                NonStandard += 1
                Regs.append(Reg)
        else:
            NonStandard += 1
            Regs.append(Reg)
    else:
        NonStandard += 1
        Regs.append(Reg)
    print(NonStandard)
    
                                    



Speeds = []

for i in range(Regs):
    print(f"Enter data for {Regs[i]}")
    Time = int(input("Enter the time taken to pass through the sensors (Hours): ")) # Input the time
    Distance = int(input("Enter the distance between the two sensors (Miles): ")) # Input the distance
    Speeds.append(Distance/Time) # Calculate the Speed and add to list
    

for i in range(Speeds.__len__()): # Loop over all Speeds
    print(f"Vehicle {Regs[i]} was traveling at a speed of {Speeds[i]} mph") # Output the speed in a formated way

print("Finished vehicle speed test")