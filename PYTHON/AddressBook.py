#Searches the file by a name returning all those who match
def NameSearch():
    counter = 0
    Name = input("Enter a name: ")
    file = open("test.csv", "r")
    line = file.readline()
    while(line):
        data=line.split(",")
        if data[0]==Name:
            print("Address:",data[1])
            print("City:",data[2])
            print("Phone Number:",data[3] + "\n")
            counter = 1
        line=file.readline()
        if counter == 0:
            print("No data found!\n")
    file.close()

#Searches the file by city returning all those who match
def CitySearch():
    counter = 0
    City = input("Enter a city: ")
    file = open("test.csv", "r")
    line = file.readline()
    while(line):
        data=line.split(",")
        if data[2]==City:
            print("Name:",data[0])
            print("Address:",data[1])
            print("Phone Number",data[3] + "\n")
            counter = 1
        line=file.readline()
    if counter == 0:
        print("No data found!\n")
    file.close()

#Searches the file by phone number returning all those who match
def PhoneSearch():
    counter = 0
    try:
        Phone = int(input("Enter a Phone Number: "))
    except ValueError:
        print("Please only enter numbers!\n")
        run_program()
    file = open("test.csv","r")
    line = file.readline()
    while(line):
        data=line.split(",")
        value = int(data[3])
        if value==Phone:
            print("Name:",data[0])
            print("Address:",data[1])
            print("City:",data[2] + "\n")
            counter = 1
        line=file.readline()
    if counter == 0:
        print("No data found!\n")
    file.close()

def DataInput():
    Name = input("Enter a name: ")
    Address = input("Enter an address: ")
    City = input("Enter a city: ")
    try:
        Phone = input("Enter a phone number: ")
        int(Phone)
        file = open("test.csv", "a")
        file.write("\n" + Name + "," + Address + "," + City + "," + Phone)
        file.close()
        print("Contact added!\n")
    except ValueError:
        print("Please only use numbers!")
        DataInput()

#Runs the program
def run_program():
    while True:
        print("Address Book Program")
        choice = input("1. Search by Name\n2. Search by city\n3. Search by phone number\n4. Add a new contact\n5. Exit program\n")
        if choice == "1":
            NameSearch()
        elif choice == "2":
            CitySearch()
        elif choice == "3":
            PhoneSearch()
        elif choice == "4":
            DataInput()
        elif choice == "5":
            exit()
        else:
            print("Please only enter 1, 2 or 3!")

run_program()