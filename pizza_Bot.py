# pizza bot programme
# 09/03/22
# Bugs: phone number input allows letters
#       name input allows numbers 

import random 
from random import randint


# list of random name

names = ["Herbert", "Gary", "Lisa", "Laquisha", "Abebe", "Dwayne", "Lee", "Virash", "Pam", "Muhhamed"]

# List of pizza names and prices

pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe', 
                'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']

pizza_prices = ['8.50', '8.50', '8.50', '8.50', '8.50', '8.50', '8.50', '13.50', '13.50', '13.50', '13.50', '13.50']

# List to store order pizzas
order_list = []
# List to store pizzas price
order_cost = []

# Customer details dictionary
customer_details = {}


# validates inputs to check where they are blank

def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("Please do not leave this blank")



# welcome with random names

def welcome():
    '''
    Purpose: To generate a random name from the list and print out onto welcome message
    Paremeters: None
    Returns: None
    '''
     
    num = randint(0,9)
    name = (names[num])
    print("Welcome to Dream Pizzas!")
    print("My name is",name, "")
    print("I will be here to help you order your delicious Dream Pizza!")


# menu with pick up or delivery

def order_type():
    print ("Is your order pick up or delivery?")
    print ("For delivery please enter 1")
    print ("For pick up please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number = "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Delivery!")
                    delivery_info()
                    break
                elif delivery == 2:
                    print ("Pickup!")
                    pickup_info()
                    break
            else:
                print ("!!! The number must be one or two !!!")
        except ValueError:
            print ("!!! I'm sorry, but that was not a valid input !!!")
            print ("!!! please enter 1 or 2 !!!")


# pick up Information - name and phone number

def pickup_info():
    question = ("Please enter your name: ")
    customer_details ['name'] = not_blank(question)
    #print (customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print(customer_details)


# Delivery information - name address and phone

def delivery_info():
    question = ("Please enter your name: ")
    customer_details ['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
   

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name: ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])
    print (customer_details)




# pizza menu

def menu():
    number_pizzas = 12
    for count in range(number_pizzas):
        print("{} {} ${}" .format(count+1, pizza_names[count], pizza_prices[count]))



# Choose total number of pizza's - max 5
def order_pizza():

# ask for total number of pizzas for order
    num_pizzas = 0
    while True:
        try:
            num_pizzas = int(input("How many pizzas do you want to order? "))
            if num_pizzas >= 1 and num_pizzas <= 5:
                break
            else:
                print("Order must be between 1 and 5") 
        except ValueError:
            print ("*** I'm sorry, but that was not a valid input... ***")
            print ("*** please enter a number between 1 and 5***")

# choose pizza from menu
# pizza order - from menu - print each pizza ordered with cost
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                    try:
                        pizza_ordered = int(input("Please choose your pizzas by entering the number from the menu: "))
                        if pizza_ordered >= 1 and pizza_ordered <= 12:
                            break
                        else:
                            print("!!! Your order must be between 1 and 12 !!!") 
                    except ValueError:
                        print ("!!! I'm sorry, but that was not a valid number !!!")
                        print ("!!! Please enter a number between 1 and 12 !!!")
            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas-1











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
    order_type()
    menu()
    order_pizza()

main()
