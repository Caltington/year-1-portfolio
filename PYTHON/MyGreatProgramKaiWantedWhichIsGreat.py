import random

def login():
    inputusername = input("Enter your username: ")
    inputpassword = input("Enter your password: ")
    username = "Leemaster67"
    password = "TheRealLeemaster67!"
    if inputusername == username:
        if inputpassword == password:
            print("Valid login")
            print("Welcome", username + "!\n")
            menu()
        else:
            print("Invalid password")
            login()
    else:
        print("Username not found!")
        login()

def Add_Student():
    student_ID = random.randint(1000,9999)
    firstname = input("Enter the student's first name: ")
    secondname = input("Enter the student's second name: ")
    dateofbirth = input("Enter student's date of birth: ")
    address = input("Enter student's address: ")
    phonenumber = input("Enter the student's phone number: ")
    gender = input("Enter the student's gender: ")
    tutorgroup = input("Enter the student's tutor group: ")
    with open("StudentDatabase.csv", "a") as file:
        file.write(str(student_ID) + "," + firstname + "," + secondname + "," + dateofbirth + "," + address + "," + phonenumber + "," + gender + "," + tutorgroup)
    print("Added to database")
    menu()

def Search_Student():
    student = input("Enter the student ID: ")
    with open("StudentDatabase.csv", "a") as file:
        line = file.readline()
        while(line):
            data=line.split(",")
            if data[0] == student:
                print(data)
            else:
                print("nothing found")
    menu()

def menu():
    print("Tutor Group Program")
    print("Do you wish to add a student, search for a student, generate a report or log out?")
    choice = input("1. Add student\n2. Search for student\n3. Generate report\n4. Log out\n")
    if choice == "1":
        Add_Student()
    elif choice == "2":
        Search_Student()
    elif choice == "3":
        pass
    elif choice == "4":
        print("Logging out...")
        exit()
    else:
        print("Invalid choice!")
        print("Only enter 1, 2, 3 or 4!")
        menu()

login()
