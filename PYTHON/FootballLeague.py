import pandas as pd

def Display():
    with open("FootballLeagueTable.csv", "r") as file:
        df = pd.read_csv(file)
        print(df)
        menu()

def ModifyTeams():
    option = input("Do you wish to add or remove teams?\n1. Add\n2. Remove\n3. Return to menu\n")
    if option == "1":
        AddTeams()
    elif option == "2":
        RemoveTeams()
    else:
        print("Invalid input")
        menu()

def AddTeams():
    team = input("Enter team name: ")
    wins = input("Enter current wins: ")
    draws = input("Enter current draws: ")
    losses = input("Enter currents losses: ")
    with open("FootballLeagueTable.csv", "a") as file:
        file.write(team + "," + wins + "," + draws + "," + losses + "\n")
    ModifyTeams

def RemoveTeams():
    pass

def ModifyPoints():
    pass

def PointsUpdate():
    df = pd.read_csv("FootballLeagueTable.csv")
    counter = 0
    with open("FootballLeagueTable.csv", "r") as file:
        df.loc[counter, "Points"]
        line = file.readline()
        while(line):
            data=line.split(",")
            wins = data[1]
            draws = data[2]
            wins = wins * 3
            points = wins + draws
            counter + 1
            line = file.readline()
    print(df)
    menu()

def menu():
    option = input("Football League Table\n\n1. Display table\n2. Add or remove a team\n3. Modify points\n4. Exit\n")
    if option == "1":
        Display()
    elif option == "2":
        ModifyTeams()
    elif option == "3":
        ModifyPoints()
    elif option == "4":
        exit()
    else:
        print("Invalid input")

PointsUpdate()
#menu()