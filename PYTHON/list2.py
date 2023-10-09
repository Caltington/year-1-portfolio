drivers = ["Kevin Magnussen", "Lando Norris", "Charles Leclerc", "Sebastian Vettel"]
wages = [3, 5, 17, 21]

length = len(drivers)
totalWage = 0
for x in range(0,length):
    print(drivers[x], wages[x])
    totalWage = totalWage + wages[x]
print("The total wage is:", totalWage)