# Bugs
# will only work for valid inputs "d" or "p"

# menu so that user can choose either pick up or delivery

print ("*** Do you want your order delivered or are you picking it up? ***")

print ("*** For delivery enter d or enter p for pick up ***")

delivery = input()

if delivery == "d":
    print ("Delivery!")

elif delivery == "p":
    print ("Pickup!")