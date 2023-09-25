#Fancy little introduction thing
print("Sleep Calculator")
print("**** Hello! ****")

#Calculates the hours per week with the hours per night and prints it
hourspernight = input("How many hours per  night do you sleep? ")
hoursperweek = int(hourspernight) * 7
print ("You sleep",hoursperweek,"hours per week")

#Calculates the hours per month and rounds it
hourspermonth = float(hoursperweek) * 4.35
hourspermonth = round(hourspermonth)
print ("You sleep",hourspermonth,"hours per month")

#Calculates the days per month slept and prints it
dayspermonth = hourspermonth / 24
print ("You sleep", dayspermonth, "days per month")