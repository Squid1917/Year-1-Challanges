print("Hello Welcome to the troubleshooter: ")
Query = input("Enter query: ").upper()
if Query.__contains__("PHONE"):
    if "BATTERY" not in Query:
        if "SCREEN" not in Query:
            if "KEYBOARD" not in Query:
                if "SPEAKER" not in Query:
                    if "SCREEN" not in Query:
                        if "MICROPHONE" not in Query:
                            print("Sorry i cant help with that yet")
                        else:                           
                            print("Replace the microphone")
                    else:                           
                        print("Replace the screen")
                else:                           
                    print("Replace the speaker")
            else:                           
                print("Replace the keyboard")
        else:                           
            print("Replace the screen")
    else:                           
        print("Replace the battery")
else:                           
    print("Sorry we only troubleshoot phones, please specify that you have phone problem")