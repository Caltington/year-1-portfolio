reg = "N/A"

def VehicleInput():
    reg = input("Enter a registration")
    time = int(input("Please enter the time the vehicle took in seconds! "))
    distance = 500 #distance is 100m
    speedlimit = 60 #speedlimit is 60km/h
    speed = (distance/10)/(time/36)
    if speed > speedlimit:
        print("Vehicle was speeding!")
        with open("Speeding.csv", "w") as file:
            file.write("\n" + reg + "," + str(speed))
    else:
        print("Vehicle was not speeding!")
    while True:
        print("Do you wish to enter a new vehicle, view a vehicle or exit?")
        choice = input("1. Repeat 2. View 3. Exit\n")
        if choice == "1":
            VehicleInput()
        elif choice == "2":
            VehicleViewStart()
        elif choice == "3":
            exit()
        else:
            print("Please enter only 1, 2 or 3!")

def VehicleViewStart():
    while True:
        print("Do you wish to view a specific vehicle or return to menu?")
        choice = input("1. Specific 2. Exit\n")
        if choice == "1":
            VehicleSpecifc()
        elif choice == "2":
            Start()
        else:
            print("Please enter only 1, 2!")


def VehicleSpecifc():
    VehicleSelected = input("Enter the registration of the vehicle: ")
    with open("Speeding.csv", "r") as file:
        line = file.readline()
        while(line):
            data=line.split(",")
            if data[0] == VehicleSelected:
                print(VehicleSelected + " was speeding at a speed of " + data[1] +"km/h")
                counter = 1
            line = file.readline()
        if counter == 0:
            print("No data found!")
    VehicleViewStart()

def Start():
    while True:
        print("Do you wish to input vehicles, view vehicles or exit? ")
        choice = input("1. Input\n2. View\n3. Exit\n")
        if choice == "1":
            VehicleInput()
        elif choice == "2":
            VehicleViewStart()
        elif choice == "3":
            exit()
        else:
            print("Please enter only 1, 2 or 3!")

Start()