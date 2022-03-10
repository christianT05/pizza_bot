# List to store order pizzas
order_list = ['Margherita','Hawaiian', 'Vegan', 'BBQ Chicken Deluxe']
# List to store pizzas price
order_cost = [8.50, 8.50, 8.50, 13.50]

customer_details = {'Name': 'Mark', 'Phone': '022 333 4444', 'House Number': '45', 'Street': "Deez", "Suburb": "Howick"}

def print_order():
    total_cost = sum(order_cost)
    print("Customer Details...")
    print(f"Customer Name: {customer_details['Name']} \nCustomer Phone: {customer_details['Phone']} \nCustomer Adress: {customer_details['House Number']} {customer_details['Street']} {customer_details['Suburb']}")
    print()
    print("Order Details...")
    count = 0
    for item in order_list:
        print("Ordered: {}  Cost: ${:.2f}".format (item, order_cost[count]))
        count = count+1
    print()
    print("Total Cost...")
    print(f"${total_cost:.2f}")

print_order()