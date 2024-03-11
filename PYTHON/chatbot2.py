answer = input("Describe the issue\n")
if "wet" in answer or "water" in answer or "soggy" in answer or "spilt" in answer or "sink" in answer or "toilet" in answer or "bath" in answer:
    print("Put the phone in rice - Intern Technician Sandick")
elif "drop" in answer or "dropped" in answer or "fell" in answer or "fallen" in answer:
    print("Take it to a repair store")
elif "virus" in answer or "stolen" in answer or "malware" in answer or "hacked" in answer or "freezing" in answer:
    print("Wipe the phone and secure accounts associated")
elif "snapped" in answer or "in half" in answer or "destroyed" in answer or "pieces" in answer or "blown up" in answer or "blew up" in answer:
    print("Fly high phone")
elif "battery" in answer or "out" in answer or "ran" in answer or "dead" in answer:
    print("Charge the phone first and if it does not charge arrange for it to be reviewed by a repair man")
elif "screen" in answer or "display" in answer or "blank" in answer or "off" in answer:
    print("Make sure the phone is charged")
elif "forgot" in answer or "password" in answer or "locked" in answer or "passcode" in answer:
    print("Try to find somewhere you may have noted down the password. If you cannot visit a phone shop for assistance")
elif "slow" in answer or "takes forever" in answer:
    print("Try removing apps and clearing data if not wipe the phone because there could be a virus")
else:
    print("Issue not found")