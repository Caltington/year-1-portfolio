Teams = ["Ferrari", "Williams", "Haas", "Racing Point"]
print("Current bonus payment:",Teams[0])

print(Teams[1], "will be the rival!")

Teams[3] = "Aston Martin"

Teams.append("Garry")
Teams.append("BARRYY")
print(Teams)

member = int(input("Which member do you wish to replace? 0-5 "))
new = input("Enter the name of the new member: ")
Teams[member] = new
print(Teams)