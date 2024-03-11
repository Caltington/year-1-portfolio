q1 = input("Does your phone turn on?\n")
if q1.upper() == "YES":
    q2 = input("Can you unlock the phone?\n")
    if q2.upper() == "YES":
        q3 = input("Do all the buttons work?\n")
        if q3.upper() == "YES":
            q4 = input("Does the battery decrease fast?\n")
            if q4.upper() == "YES":
                print("Visit EXAMPLE for battery health information")
            else:
                q5 = input("Is there a virus?\n")
                if q5.upper() == "YES":
                    print("Tips on how to wipe phone")
                else:
                    print("No problem with phone")
        else:
            print("Visit a repair store to fix the buttons")
    else:
        q6 = input("Did you forget the password?\n")
        if q6.upper() == "YES":
            print("How to reocver phone")
        else:
            print("L")
else:
    q7 = input("Did the phone go in water?\n")
    if q7.upper() == "YES":
        print("put it in rice")
    else:
        q8 = input("Is the phone charged?\n")
        if q8.upper() == "YES":
            q9 = input("Are the parts damaged?\n")
            if q9.upper() == "YES":
                print("Visit repair store")
            else:
                print("L")

def answer(answeer):
    

    