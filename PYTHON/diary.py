from datetime import date

def write():
    text = input("Enter the entry: ")
    today = str(date.today())
    with open("diary.txt", "a") as file:
        file.write(today + ": " + text + "\n")
        print("Entry was written")

def read():
    with open("diary.txt", "r") as file:
        print("\n")
        print(file.read())

def start():
    while True:
        print("Do you wish to read the diary or write to it?")
        choice = input("1. Read \n2. Write\n")
        if choice == "1":
            read()
        elif choice == "2":
            write()
        else:
            print("Please only enter 1 or 2")

start()