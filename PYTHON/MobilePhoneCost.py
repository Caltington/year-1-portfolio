#Name and network input
name = input("Enter your name: ")
network = input("Enter your network: ")

#Calculates the price of the minutes and texts
minutespermonth = input("How many minutes have you used this month: ")
numberoftexts = input("How many texts have you sent this month: ")
priceofminutes = int(minutespermonth) * 0.1
priceoftexts = int(numberoftexts) * 0.05

#Calculates the total cost for the month for both vat and non-vat
totalprice = priceofminutes + priceoftexts
vattotalprice = totalprice * 1.2
print("The price this month is ", totalprice," pence")
print("The price this month including vat is ",vattotalprice," pence")
