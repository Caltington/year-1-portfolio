import pandas as pd

def BookRoom():
    name = input("Enter booking name: ")
    room = input("Enter room number: ")
    numbercheck(room)
    print("Select a service\n1. Normal\n2. Premium")
    service = input()
    if service == "1":
        print("Normal service selected")
        service = "normal"
    elif service == "2":
        print("Premium service selected")
        service = "premium"
    else:
        print("Only enter 1 or 2")
        BookRoom()
    startdate = input("Enter start date in dd/mm/yy format: ")
    days = input("Enter the number of days you will stay: ")
    numbercheck(days)
    DateValidation(startdate)
    with open("HotelManagement.csv", "a") as file:
        file.write(name + "," + room + "," + service + "," + startdate + "," + str(days) + "\n")
    print("Added to database")
    #Get a billing csv and write it to it
    with open("Billing.csv", "a") as file:
        total = days * 100
        if service == "normal":
            pass
        else:
            total = total + 150
        file.write(name + "," + str(total) + "\n")
    print("Added to database")
    Start()

def ViewRoom():
    with open("HotelManagement.csv", "r") as file:
        df = pd.read_csv(file)
    print(df)
    #open rooms csv
    #convert to pandas
    #output pandas
    Start()

def ViewBilling():
    with open("Billing.csv", "r") as file:
        df = pd.read_csv(file)
    print(df)
    Start()

def GuestRecords():
    #Check date is before today 
    #Check that date + days is before today
    pass

def numbercheck(x):
    try:
        int(x)
    except ValueError:
        print("Value is not a number")
        BookRoom()

def DateValidation(date1):
    pass
    #Make it so it makes sure both dates are valid format
    #Make sure end date is after start date

def Start():
    print("\nWelcome to hotel management system!\n")
    answer = input("1. Book a room\n2. View rooms\n3. View billing\n4. View guest records\n5. Exit\n")
    if answer == "1":
        BookRoom()
    elif answer == "2":
        ViewRoom()
    elif answer == "3":
        ViewBilling()
    elif answer == "4":
        GuestRecords()
    elif answer == "5":
        exit()
    else:
        print("Invalid answer")
        Start()

Start()