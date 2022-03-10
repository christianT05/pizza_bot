# List to store order pizzas
order_list = ['Margherita','Hawaiian', 'Vegan', 'BBQ Chicken Deluxe']
# List to store pizzas price
order_cost = [8.50, 8.50, 8.50, 13.50]

customer_details = {'Name': 'Mark', 'Phone': '022 333 4444', 'House': '45', 'Street': "Deez", "Suburb": "Howick"}


#print("\n",customer_details['Name'],"\n",customer_details['Phone'],"\n",customer_details['House'],"\n",customer_details['Street'],"\n",customer_details['Suburb'])

print("\n Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb:\n{}".format(customer_details['Name'],customer_details['Phone'],customer_details['House'],customer_details['Street'],customer_details['Suburb']))
count = 0
for item in order_list:
    print("Ordered: {}  Cost:  ${:.2f}".format (item, order_cost[count]))
    count = count+1