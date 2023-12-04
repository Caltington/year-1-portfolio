def login():
    inputusername = input("Enter your username: ")
    inputpassword = input("Enter your password: ")
    username = "Leemaster67"
    password = "TheRealLeemaster67!"
    if inputusername == username:
        if inputpassword == password:
            print("Valid login")
            print("Welcome", username, "!\n")
            menu()
        else:
            print("Invalid password")
            login()
    else:
        print("Username not found!")
        login()

def menu():
    print("Tutor Group Program")
    print("Do you wish to add a student, search for a student, generate a report or log out?")
    choice = input("1. Add student\n2. Search for student\n3. Generate report\n4. Log out\n")
    if choice == "1":
        pass
    elif choice == "2":
        pass
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
