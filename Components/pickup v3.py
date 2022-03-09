# Customer details dictionary
customer_details = {}

# Basic Instructions
print("Please enter the pick up information")

# Customer Name not blank
valid = False
while not valid:
    customer_details ['name'] = input("Please enter your name = ")
    if customer_details ['name'] != "":
        print (customer_details ['name'])
        break

    else:
        print("Please do not leave this blank")

# Customer Phone Number not blank
valid = False
while not valid:
    customer_details['phone'] = input("Please enter your phone number = ")
    if customer_details['phone'] != "":
        print (customer_details['phone'])
        break

    else:
        print("Please do not leave this blank")

