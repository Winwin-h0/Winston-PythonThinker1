import random
# Task 1​

# ​
# Create 2 parallel lists with 4 values each.​
# fruits: List of fruits​
# prices: List of prices of the fruits​
# Use a for loop to print each fruit with its price in this format:​
# <fruit> costs $<price>.

# fruits = ["apple", "pear", "grapes", "blueberries"]
# prices = [0.60, 0.70, 1.00, 1.00]
# for i in range(len(fruits)):
#     print(f"{fruits[i]} costs ${prices[i]}. ")

# groceries = ["apple", "banana", "coconut", "pineapple", "pear"]
# stocks = []
# for i in range(len(groceries)):
#     stocks.append((random.randint(0,50)//2))


# # Task 2a​

# # Create a program that: ​

# # checks a supermarket’s inventory stock levels and ​
# # allows the user to search for an item.​
# # Loop through the given lists to check the status of the stock, if the stock is:​
# # Equal to 0 → Status: Out of Stock​
# # Less than 10 → Status: Low Stock​
# # 10 or more → Status: Well Stocked​
# # Print the result in this format:​
# # Item: <item> | Stock: <stock> | Status: <status>​

# for i in range(len(groceries)):
#     stock = stocks[i]
#     if stock == 0:
#         status = "Out of stock"
#     elif stock < 10:
#         status = "Low stock"
#     else:
#         status = "Well stocked"
#     print(f"Item: {groceries[i]} | Stock: {stock} | Status: {status} ")
    

# # Task 2b
# # Ask the user to input an item to check.
# user_select = input("Item to check? ")

# # Check if the item is in the list
# # a) If the item is in the list:
# #    - Find its index
# #    - Print the result in this format:
# #      - Result: We have <stock> <item>(s) remaining.
# if user_select in groceries:
#     index_of_thing = groceries.index(user_select)
#     print(f"We have {stocks[index_of_thing]} of {user_select}(s) remaining ") #stocks[]
# # b) If the item is not in the list:
# #    - Print an error message
# #      - Error: Item not found in database.
# else:
#     print("Error: Item not found in database.")


# Task 3a
# Create a program that:
# - add items to a shopping list
# - calculate their costs
# - print a receipt

# 1) Print the current shopping list.
# 2) Ask the user how many more items they want to buy.
# 3) Use a for loop to ask what the items are and append it to the shopping list.
# 4)Print the updated shopping list.
# shopping = ["pencil", "marker", "white board"]
# print(shopping)
# add_num_item = int(input("How many more items are you buying? "))
# for i in range(add_num_item):
#     new_item = input("What are the items? " )
#     shopping.append(new_item)
# print(shopping)

# # Task 3b
# # 1) Create an empty list to store the prices: price_list

# # 2) For each item in the shopping list:
# #    a) Ask for price
# #    b) Ask for quantity
# #    c) Multiply the price and quantity and append it to the price list

# # 3) Print the price list
# price_list = []
# for i in range(len(shopping)):
#     price = float(input(f"What is the price for {shopping[i]}? "))
#     qty = int(input("How much you need? "))
#     item_total_price = price * qty
#     price_list.append(item_total_price)
# print(price_list)

# # Task 3c
# # 1) Use a for loop to print the shopping list and price list following the format below.
# # 2) Add up the total cost in the price list and print it.

# # total = 0
# total = 0
# print("----order summery----")
# for i in range(len(price_list)):
#     print(f"Item {i + 1} - {shopping[i]}: ${price_list[i]}")
#     total += price_list[i]
# print(f"total : ${total}")




# print(f"Total: ${total}")
# ---ORDER SUMMARY---
# Item 1: $XXX
# Item 2: $YYY
# ...
# Item Last: $ZZZ
# --------------------
# Total: $AAA

# import random
# # Task 4a
# # Create a list of possible moves:
# # ["scissors", "paper", "stone"]

# moves = ["scissors", "paper", "stone"]

# # Initialize 2 variables:
# # player_score
# # computer_score

# player_score = 0
# computer_score = 0

# # Use a while loop to ask for the user’s move while player_score and computer_score is less than 3.
# while player_score > 3 and computer_score > 3:
#     user_move = input("Rock, Paper or Scissors?")
# # Task 4b
# # In the while loop:
# # Import the random library, use random.choice() to let the computer pick from the move list and print it.
   
#     comp_move = random.choice(moves)
#     print(comp_move)
# # Compare the user’s choice and computer’s choice to determine the result.
#     if comp_move == "rock" and user_move == "paper":
#         player_score += 1
#     elif comp_move == "rock" and user_move == "scissors":
#         computer_score += 1
#     elif comp_move == "scissors" and user_move == "rock":
#         player_score += 1
#     elif comp_move == "scissors" and user_move == "paper":
#         computer_score += 1
#     elif comp_move == "paper" and user_move == "scissors":
#         player_score += 1
#     elif comp_move == "paper" and user_move == "rock":
#         computer_score += 1
#     else:   
#         player_score = player_score
#         computer_score = computer_score
        
# Increment player_score or computer_score depending on the result.

# Print the result and scores.

# Task 4c
# Print the final result after the while loop has ended.
# Modify the loop to check for invalid choices.



import random

moves = ["rock", "paper", "scissors"]


player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    user_move_choice = int(input("Rock(0), Paper(1) or Scissors(2)? "))
    if user_move_choice > 2:
        print("Please key in 0 - 2")
        continue
    user_move = moves[user_move_choice]

    comp_move = random.choice(moves)
    print(comp_move)

    if comp_move == "rock" and user_move == "paper":
        player_score += 1
    elif comp_move == "rock" and user_move == "scissors":
        computer_score += 1
    elif comp_move == "scissors" and user_move == "rock":
        player_score += 1
    elif comp_move == "scissors" and user_move == "paper":
        computer_score += 1
    elif comp_move == "paper" and user_move == "scissors":
        player_score += 1
    elif comp_move == "paper" and user_move == "rock":
        computer_score += 1
    else:   
        player_score = player_score
        computer_score = computer_score
        
    print(f"computer score : {computer_score}")
    print(f"your score : {player_score}")

if computer_score > player_score:
    print(f"The computor has {computer_score}, and you have {player_score}, so the winner is... the computer!")
el