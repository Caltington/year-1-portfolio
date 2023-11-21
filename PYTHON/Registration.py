thing = False

def UpperCheck(letter):
    thing = letter.isupper()
    if thing == True:
        return thing
    else:
        print("Incorrect Value Entered (letter error)")
        RegistrationInput()

def NumberCheck(letter):
    thing = letter.isnumeric()
    if thing == True:
        return thing
    else:
        print("Incorrect Value Entered (number error)")
        RegistrationInput()


def RegistrationInput():
    RegistrationText = input("Enter a registration ")
    if len(RegistrationText) == 8:
        outcome = UpperCheck(RegistrationText[0])
        if outcome == True:
            outcome = UpperCheck(RegistrationText[1])
            if outcome == True:
                outcome = NumberCheck(RegistrationText[2])
                if outcome == True:
                    outcome = NumberCheck(RegistrationText[3])
                    if outcome == True:
                        outcome = UpperCheck(RegistrationText[5])
                        if outcome == True:
                            outcome = UpperCheck(RegistrationText[5])
                            if outcome == True:
                                outcome = UpperCheck(RegistrationText[6])
                                StoreReg(RegistrationText)
    else:
        print("Registration is invalid (too short)")     

def StoreReg(Reg):
    with open("ValidDatabase.txt", "a") as file:
        file.write(Reg + "\n")


RegistrationInput()