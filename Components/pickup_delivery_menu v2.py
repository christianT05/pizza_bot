# Bugs
# will only work for valid inputs "d" or "p"
# invalid input triggers else statement but does not ask for inout again
# menu so that user can choose either pick up or delivery

print ("*** Do you want your order delivered or are you picking it up? ***")

print ("*** For delivery enter d ***")
print ("*** For pick up enter p ***")

delivery = input()

if delivery == "d":
    print ("Delivery!")

elif delivery == "p":
    print ("Pickup!")

else:
    print ("*** That was not a valid input... ***")