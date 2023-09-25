temp = int(input("Enter temperature to change: "))
if(input("C -> F (1)      F-> C (2) ") == '1'):
    #*Converts the value and prints it
    print("Fahrenheit: " + str(temp *9/5 +32))
else:
    #*Converts the value and prints it
    print("Celsius: " + str((temp-32)*5/9))
