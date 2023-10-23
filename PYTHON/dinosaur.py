def Question1():
    while True:
        print("\nIs the dinosaur a herbivore?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            Question2A()
        elif choice == "2":
            Question2B()
        else:
            print("Please use 1 or 2!")

def Question2A():
    while True:
        print("\nIs your dinosaur tall?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            Answer("Brachiosaurus")
        elif choice == "2":
            Answer("Stegosaurus")
        else:
            print("Please use 1 or 2!")

def Question2B():
    while True:
        print("\nDoes it fly?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            Question3A()
        elif choice == "2":
            Question3B()
        else:
            print("Please use 1 or 2!")

def Question3A():
    while True:
        print("\nIs the tail short?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            Answer("Pterodactyl")
        elif choice == "2":
            Answer("Rhamphorhynchoids")
        else:
            print("Please use 1 or 2!")

def Question3B():
    while True:
        print("\nIs it tall?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            Answer("T-Rex")
        elif choice == "2":
            Question4B()
        else:
            print("Please use 1 or 2!")

def Question4B():
    while True:
        print("\nDoes it spit?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            Answer("Dilophosaurus")
        elif choice == "2":
            Answer("Velociraptor")
        else:
            print("Please use 1 or 2!")

def Answer(dinosaur):
    print("\nYour dinosaur is a", dinosaur + "!")
    while True:
        print("Do you want to play again?")
        choice = input("1. Yes\n2. No\n")
        if choice == "1":
            ProgramStart()
        elif choice == "2":
            exit()
        else:
            print("Please use 1 or 2!")
    

def ProgramStart():
    while True:
        print("Dinosaur Identifier")
        choice = input("1. Start\n2. Exit\n")
        if choice == "1":
            Question1()
        elif choice == "2":
           exit()
        else:
            print("Please use 1 or 2!")

ProgramStart()