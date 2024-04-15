import random

def start():
    thing = input("Which dice do you want?\n1. 4 Sided\n2. 6 Sided\n3. 12 Sided\n")
    if thing == "1":
        dice(4)
    elif thing == "2":
        dice(6)
    elif thing == "3":
        dice(12)
    else:
        print("Invalid Input ")
        start()

def dice(sides):
    answer = random.randint(1,sides)
    print("The " + str(sides) + " sided dice rolled " + str(answer) + "\n")
    start()

start()

