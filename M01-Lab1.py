"""
Project/File Name: ___________________________
Author:           ___________________________
Date Created:     ___________________________
Last Modified:    ___________________________

Purpose:          [Brief description of what this file/project does]

Dependencies:     [List any required libraries, modules, or files]
Usage:            [How to run or use this file/project]
Inputs:           [Describe expected input, if any]
Outputs:          [Describe output, if any]
Notes:            [Any additional important information]
"""

#
"""
START
Display a welcome message to the customer
Define a menu with food items and their prices (e.g., Burger - $5, Pizza - $8, Salad - $4, Soda - $2)
Initialize total order amount to 0
LOOP (repeat until the customer is done ordering):
    Display the menu with item numbers and prices
    Ask the customer to enter the item number they want to order
    Ask the customer to enter the quantity for that item
    Calculate the cost for this item:
    item cost = price of item * quantity
    Add the item cost to the total order amount
    Ask the customer if they want to order another item (yes/no)
    IF the answer is "no":
        Exit the loop
Display the total order amount to the customer
Display a thank you message
END
"""
menu = { 
    1: {"name": "Burger", "price": 7}, 
    2: {"name": "Hotdog", "price": 3}, 
    3: {"name": "Drink", "price": 2},
    4: {"name": "Cake", "price": 5},
    5: {"name": "Pizza Slide", "price" : 5},
}
# Variable to hold/store total order cost 
total_order_cost = 0

# print welcome message to the user
name = input ("Hello, what's your name? \n")
print ("welcome" + name + "," "This is the cafe!")

while True: 
    print("\nMenu: ")
    # Get item number that custumer wants to order
    # Using try/except to handle invalid inputs
