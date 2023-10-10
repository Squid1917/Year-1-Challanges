def CheckPassword(password):
    strength = "Medium"
    if(len(password) < 6): #* Check if to short
        print("Password To Short")
        strength = "Weak"
        return False
    elif(len(password) > 12): #* Check if to long
        print("Password To Long")
        strength = "Weak"
        return False
    if(any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password)):
        strength = "STRONG"
        print(strength)
        return True
    elif(password.isdigit()): #* Check if all digits
        print("Password Can Not Be All Digits")
        strength = "Weak"
        return False
    elif(password.isalpha()): #* check if all letters
        print("Password Can Not Be All Letters")
        strength = "Weak"
        return False
    elif(password.isalnum()): #* check if has two cases
        strength = "Medium"
        print(strength)
        return True
    elif(password.isupper()): #* Checks if all upper
        print("Password Can Not Be One Case")
        strength = "Weak"
        return False
    elif(password.islower()): #* Checks if all lower
        print("Password Can Not Be One Case")
        strength = "Weak"
        return False
    

while True:
    password = input("Enter Password: ")
    if CheckPassword(password):
        print("Password Accepted")
        break

print("Well Done")