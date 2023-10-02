password = " "
count = 0 
while (password != "changeme"): 
 password = input("Enter your password: ")
 count = count + 1 
print ("Accepted")
print("You took " + str(count) + " attempts!")  

