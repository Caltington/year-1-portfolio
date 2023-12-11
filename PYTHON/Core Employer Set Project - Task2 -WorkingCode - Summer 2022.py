import pandas as pd


houses = [['LONDON','Terraced', 3, 735000], ['CARDIFF', 'Semi-Detached', 2, 100000], ['LEEDS','Terraced', 3, 245000], ['LONDON','Semi-Detatched', 1, 240000]]
sales = []
ourregions = ['LONDON', 'LEEDS', 'CARDIFF', 'BRISTOL']    
property_types =  ['TERRACED', 'SEMI-DETATCHED','DETATCHED']

def new_property():
    #Region type check and input
    for i, item in enumerate(ourregions, 1):
        print(i, item)
    region_check = False
    while not region_check:
        try:
            regioninput = int(input('Please select a region: '))  
            if regioninput > 0 and regioninput < len(ourregions)+1:
                region_check = True
        except:
            print('ERROR PLEASE ENTER A VALID REGION')
    region = ourregions[regioninput-1]


    #Property type check and input
    for i, item in enumerate(property_types, 1):
        print(i, item)
    property_check = False
    while not property_check:
        try:
            propertyinput = int(input('Please select a property type: '))  
            if propertyinput > 0 and propertyinput < len(property_types)+1:
                property_check = True
        except:
            print('ERROR PLEASE ENTER A VALID PROPERTY TYPE')
    propertytype = property_types[propertyinput-1]
    
    bedroom_check = False
    while bedroom_check == False:
        try:
            bedrooms = int(input("Enter the number of bedrooms in the house: "))
            bedroom_check = True
        except:
            print("Invalid input! Please enter a number ")
    
    price_check = False
    while price_check == False:
        try:
            price = int(input("Enter the price of the house: "))
            price_check = True
        except:
            print("Invalid input! Please enter a number ")
    newhouse = [region, propertytype, bedrooms, price]
    print(newhouse)
    houses.append(newhouse)
    print("Property added!")



#Rewrite later to make it display data in a better way
def return_stock():
    if len(houses) == 0:
        print("No houses currently in stock!")
    else:
        stockdf = pd.DataFrame(houses, columns =['Region', 'House Type', 'Bedrooms', 'Price']) 
        print(stockdf)

#Works fine
def unique_regions():
    unique_list = []
    existing_regions = [item[0] for item in houses]
    unique_list = list(dict.fromkeys(existing_regions))
    print(unique_list)

#Works fine now
def region_search():
    print("Available Regions")
    unique_regions()
    r_check = False

    while not r_check:
        region_select= input("Please enter region: ").capitalize()
        regionarray = []
        for x in houses:
            if region_select.upper() == x[0].upper():
                r_check = True
                if x[0] == region_select.upper():
                    validhouse = x
                    regionarray.append(validhouse)
        searchdf = pd.DataFrame(regionarray, columns =['Region', 'House Type', 'Bedrooms', 'Price'])
        print(searchdf) 
        if r_check == False:
            print("Entered region is not valid")



def show_sales():
    if len(sales) > 0:
        nicedata = pd.DataFrame(sales, columns =['Forename', 'Surane', 'Property Cost', 'Total Cost']) 
        print(nicedata)
    else:
        print('No sales!')





def house_sale():
    if len(houses) == 0:
        print("No houses found!")
    else:
        sale = []
        customer_forename = input('Please enter customer forename: ')
        customer_surname = input('Please enter customer surname: ')
        for i, item in enumerate(houses, 1):
            print(i, item)

        sel_check = False
        while not sel_check:
            try:
                select = int(input('Please select a purchase: '))   
                if select > 0 and select < len(houses)+1:
                   sel_check = True
            except:
                print('ERROR PLEASE ENTER A VALID PROPERTY')

        sub_total = houses[select-1][3]
        print(sub_total)
        total_fees = 0


        if sub_total > 100000:
            total_fees += 3000+(sub_total-100000) * 0.2
        else:
            total_fees += sub_total *0.3

    

        final_total = sub_total+total_fees
        sale.append(customer_forename)
        sale.append(customer_surname)
        sale.append(sub_total)
        sale.append(final_total)
        sales.append(sale)

        print('Customer Receipt\n\n  FORENAME:{}  SURNAME: {}  PROPERTY COST:  {}  WITH STAMP DUTY:   {}'.format(*sales[-1]))
        print('\nTRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE\n')
        print (houses[select-1])
        del houses[select-1] 


#Menu, seems to work properly now
while True:
    menuselection = input(" WELCOME TO THE NEWHAVEN DASHBOARD \n\n Please select from the following menu options \n\n"
                              " 1: View current houses on market \n 2: Search for available houses in a region \n 3: Record"
                              " a sale \n 4: Add a new property for sale \n 5: Show Sales \n 6: Exit\n")


    if menuselection == "1":
        return_stock()
    elif menuselection == "2":
        region_search()
    elif menuselection =="3":
        house_sale()
    elif menuselection=="4":
        new_property()
    elif menuselection=="5":
        show_sales()
    elif menuselection == "6":
        exit()

         