# pizza bot programme
import random 
from random import randint

# list of random name
names = ["Herbert", "Gary", "Lisa", "Laquisha", "Abebe", "Dwayne", "Lee", "Virash", "Pam", "Muhhamed"]

# welcome with random names
def welcome():
    '''
    Purpose: To generate a random name from the list and print out onto welcome message
    Paremeters: None
    Returns: None
    '''
     
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizzas! ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza! ***")

# menu with pick up or delivery






# pick up Information - name and phone number






# Delivery information - name address and phone







# Choose total number of pizza's - max 5




# create a pizza menu



# pizza order - from menu - print each pizza ordered with cost









# print the order out - include if order is delivery or pick up and price of each pizza
# - total cost including any delivery charge


# ability to cancel or proceed with order




# main function

def main():
    '''
    Purpose: To run all functions
    Paremeters: None
    Returns: None
    '''
    welcome()
    

main()
