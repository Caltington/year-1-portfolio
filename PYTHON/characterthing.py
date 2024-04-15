import random

def character():
    name = input("Enter a name: ")
    strength = 10 + roll()
    skill = 10 + roll()
    print("\nName: " + name + "\nStrength: " + str(strength) + "\nSkill: " + str(skill))
    with open(name + ".txt", "w") as file:
        file.write("\nName: " + name + "\nStrength: " + str(strength) + "\nSkill: " + str(skill))


def roll():
    roll1 = random.randint(1,12)
    roll2 = random.randint(1,4)
    total = int(roll1/roll2)
    return total

character()