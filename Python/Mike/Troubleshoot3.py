CSV = open("Troubleshoot3.csv","r")
Questions = []
for Line in CSV:
    TempData = (Line.split(","))
    del TempData[-1]
    Questions.append(TempData)

Device = input("Enter Device: ")
for Question in Questions:
    if Question[0] == Device:
        Questions = Question
        del Questions[0]
        break

for Question in Questions:
    input(Question)

print("Sorry this is too complicated for me to solve at this stages")
print("Please go to a specicialised technitian for " + Device + "s")