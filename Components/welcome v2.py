import random 
from random import randint

# List of random names
names = ["Herbert", "Gary", "Lisa", "Laquisha", "Abebe", "Dwayne", "Lee", "Virash", "Pam", "Muhhamed"]
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


def main():
    '''
    Purpose: To run all functions
    Paremeters: None
    Returns: None
    '''
    welcome()
    

main()