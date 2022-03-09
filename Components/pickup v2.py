# Bug: program accepts and prints blank inputs

print("Please enter the pick up information")

# Customer Name
valid = False
while not valid:
    name = input("Please enter your name = ")
    if name != "":
        print (name)
        break

    else:
        print("Please do not leave this blank")

valid = False
while not valid:
    phone = input("Please enter your phone number = ")
    if phone != "":
        print (phone)
        break

    else:
        print("Please do not leave this blank")

print (name)
