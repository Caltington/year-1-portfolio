import random
import math

def character():
    name = input("Enter a name: ")
    strength = roll()
    skill = roll()
    print("\nName: " + name + "\nStrength: " + str(strength) + "\nSkill: " + str(skill) + "\n")
    return [name, strength, skill]

def roll():
    roll1 = random.randint(1,12)
    roll2 = random.randint(1,4)
    total = int(roll1/roll2)
    return total

def characters():
    character1 = character()
    character2 = character()
    if character1[1] >= character2[1]:
        strengthvs = character1[1] - character2[1]
    else:
        strengthvs = character2[1] - character1[1]
    strengthmodifier = int(math.floor(strengthvs /5))
    if character1[2] >= character2[2]:
        skillvs = character1[2] - character2[2]
    else:
        skillvs = character2[2] - character1[2]
    skillmodifier = int(math.floor(skillvs /5))
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("Player 1 rolled " + str(dice1))
    print("Player 2 rolled " + str(dice2))
    if dice1 == dice2:
        pass
    elif dice2 > dice1:
        character2[1] = character2[1] + strengthmodifier
        character1[1] = character1[1] - strengthmodifier
        character2[2] = character2[2]  + skillmodifier
        character1[2] = character1[2] - skillmodifier
    else:
        character1[1] = character1[1] + strengthmodifier
        character2[1] = character1[1] - strengthmodifier
        character1[2] = character1[2]  + skillmodifier
        character2[2] = character2[2] - skillmodifier
    c1life = ""
    c2life = ""
    if 0 >= character1[2]:
        character1[2] = 0
    if 0 >= character2[2]:
        character2[2] = 0
    if 0 >= character1[1]:
        c1life = "dead"
    if 0 >= character2[1]:
        c2life = "dead"
    
    if c1life == "dead":
        print(character1[0] + " died")
    else:
        print(character1[0] + " survived with " + str(character1[1]) + " strength and " + str(character1[2]) + " skill")

    if c2life == "dead":
        print(character2[0] + " died")
    else:
        print(character2[0] + " survived with " + str(character2[1]) + " strength and " + str(character2[2]) + " skill")

characters()