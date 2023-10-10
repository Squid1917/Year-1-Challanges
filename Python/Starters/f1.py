Teams = ["Ferrari", "Williams", "Haas", "Racing Point"]

print("Current bonus payment: ", Teams[0])
print("Rival", Teams[1])
Teams[3] = "Aston Martin"
Teams.append("Mclaren") 
Teams.append("Redbull")
print(Teams) 

NewTeamIndex = int(input("Enter Team To Replace (0-5): "))
NewTeam = input("Enter Team Name: ")
Teams[NewTeamIndex] = NewTeam

Drivers = ["Sebastian Vettel", "Charles Leclerc", "Kevin Magnussen", "Lando Norris"]
Wages = [21,17,3,5]
TotalWage = 0
for i in range(Drivers.__len__()):
    print(f"{Drivers[i]}: {Wages[i]}")
    TotalWage += Wages[i]

print(f"Total wage bill: £{TotalWage}000000")