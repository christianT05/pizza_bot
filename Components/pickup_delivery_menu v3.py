# menu so that user can choose either pick up or delivery

# bug: need to make it so that it only accepts 1 or 2.

print ("*** Is your order pick up or delivery? ***")

print ("*** For delivery please enter 1 ***")
print ("*** For pick up please enter 2 ***")


low = 1
high = 2

while True:
    try:
        delivery = int(input("Please enter a number = "))
        if delivery >= 1 and delivery <= 2:
         if delivery == 1:
                print ("Delivery!")
                break

         elif delivery == 2:
                print ("Pickup!")
                break
        else:
            print ("*** The number must be one or two ***")
    except ValueError:
        print ("*** I'm sorry, but that was not a valid input... ***")
        print ("*** please enter 1 or 2 ***")