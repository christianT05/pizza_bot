# list of pizza names and prices
pizza_names = ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe', 
                'Mega Meat Lovers', 'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe']

pizza_prices = ['8.50', '8.50', '8.50', '8.50', '8.50', '8.50', '8.50', '13.50', '13.50', '13.50', '13.50', '13.50']

# List to store order pizzas
order_list = []
# List to store pizzas price
order_cost = []

def menu():
    number_pizzas = 12

    for count in range(number_pizzas) :
        print("{} {} ${}" .format(count+1, pizza_names[count], pizza_prices[count]))


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


menu()
order_pizza()