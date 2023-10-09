print("Pick one of the following characters:")
print("DVA, Doomfist, Winton, Wrecking Ball Bastion, Genji, Tracer, Mercy, Ana")
q1 = input("Is your character human? Y/N ")
if q1 == "N":
    q2 = input("Is your character a robot? Y/N ")
    if q2 == "N":
        q3 = input("Is your character a gorilla? Y/N ")
        if q3 == "N":
            print("Your character is Wrecking Ball")
        else:
            print("Your character is winton")
    else:
        q4 = input("Is your character a ninja? Y/N ")
        if q4 == "N":
            print("Your character is Bastion")
        else:
            print("Your character is Genji")
else:
    q5 = input("Is your character male? Y/N " )
    if q5 == "Y":
        print("Your character is doomfist")
    else:
        q6 = input("Is your character a tank? Y/N ")
        if q6 == "Y":
            print("Your character is DVA")
        else:
            q7 = input("Is your character a sniper? Y/N ")
            if q7 == "Y":
                print("Your character is ana")
            else:
                q8 = input("Is your character British? Y/N ")
                if q8 == "Y":
                    print("Your character is Tracer")
                else:
                    print("Your character is Mercy")