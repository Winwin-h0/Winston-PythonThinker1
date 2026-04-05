# print("Hello from lesson 11")

# # Lesson 11 - AND OR NOT

# # Recap 1: Purchase Advisor
# Create a program that asks the user for the price of an item (px) and
# gives a comment based on the price:

# if:
#     px <= 5: "Sounds good!"
#     px <= 50: "Are you sure you need this?"
#     px <= 500: "Where are you getting this money from?!"
#     px > 500: "Don't even think about it!"

# price_item = int(input("Give me the price of a item."))

# if price_item <= 5:
#     print("Sounds good!")
# elif price_item <= 50:
#     print("Are you sure you need this?")
# elif price_item <= 500:
#     print("Where are you getting this money from?!")
# else:
#     print("Don't even think about it!")

# --------------------------------------------------------------------

# # Task 1: AND Operator in Simple Conditions (AND)
# You are writing a program for an amusement park that needs to check
# if both riders of a ride are above the height of 120cm. Use the 'and'
# operator to determine if value of both 'rider1' and 'rider2' are
# greater than 120.

# rider1 = 125
# rider2 = 150

# if rider1 > 120 and rider2 > 120:
#     print("You are allowed.")
# else:
#     print("Access denied.")


# --------------------------------------------------------------------

# # Task 2: Multiples of 3 and 7 (AND)
# Create a program to check if a number is both divisible by 3 and 7

# 1. Ask the user to input a number
# 2. If the number is both a multiple of 3 and a multiple of 7:
#     print "The number is divisible by 3 and 7!"

# number = int(input("Give me a number. "))

# if number % 3 == 0 and number % 7 == 0:
#     print("The number is divisible by 3 and 7")
# else:
#     print("The number is not divisible by 3 and 7")
# --------------------------------------------------------------------

# # Task 3: Identity Identifier (AND)
# Create a program that asks for user's first and last name and checks
# if it matches "James" and "Leong" respectively and print "YOU ARE
# WANTED" if true.

# user_first = input("Give me you first name.")
# user_last = input("Give me your last name.")

# if user_first == "James" and user_last == "Leong":
#     print("YOU ARE WANTED")
# else:
#     print("You are free to go.")
# --------------------------------------------------------------------

# # Task 4: 'or' Operator in Conditional Statements (OR)
# You run a go-kart business and need a program to check if at least
# 1 occupant of a 2-person go-kart is at least 18 years old.

# Use the 'or' operator to determine if value of either 'rider1' or
# 'rider2' is equal to or greater than 18.

# 'rider1' = 25
# 'rider2' = 6

# rider1 = 25
# rider2 = 6
# if rider1 >= 18 or rider2 >= 18:
#     print("Acess granted")
# else:
#     print("Acess denied")
# --------------------------------------------------------------------

# # Task 5: Ticket Pricing Machine (OR)
# Create a program that will decide on the price of a ticket based on
# user's age. Original ticket price costs $20 per person. However,
# children below the age of 12 and elderly above the age of 65 can buy
# the ticket for just $15.

# 1. Ask user for their age
# 2. Use the 'or' operator to determine if user's age is less than 12 or
#    more than 65. If true, print "Ticket price: $15"
# 3. Else, print "Ticket price: $20"

# age = int(input("What's your age?"))
# if age < 12 or age > 65:
#     print("Ticket price: $15")
# else:
#     print("Ticket price: $20")

# --------------------------------------------------------------------

# # Task 6: Input Validator (OR)
# Using the 'or' operator, create a program that prints "Valid Input"
# if the user has entered "M" or "Male" as an input. Or else, print
# "Invalid Input" instead

# 1. Ask user for input
# 2. If user input is "M" OR "Male", print "Valid Input"
# 3. Else, print "Invalid Input"
# user = input("What's your gender?")
# if user == "M" or user == "Male":
#     print("Valid input.")
# else:
#     print("Invalid input.")
# --------------------------------------------------------------------

# # Task 7: Colour filter (NOT)
# Create a program that will ask the user for a colour and print
# "Try again" if the input of the user is not "Green".

# 1. Ask user for a colour
# 2. Using the 'not' operator, check if input is not "Green".
#    If true, print "Try again"
# colour = input("What's the colour? ")
# if not colour == "green":
#     print("Try again.")
# else:
#     print("Correct")


    
# if colour != "green":
#     print("Try again")
# else:
#     print("Correct.")
# --------------------------------------------------------------------

# # Task 8: Not the Right Day (NOT)
# Create a program that asks the user for the day of the week. If the
# input is not "Saturday", the program should print "It's not the
# weekend yet!"

# 1. Ask the user for the day of the week.
# 2. Using the 'not' operator, check if the input is not "Saturday".
# 3. If true, print "It's not the weekend yet!"

# day = input("What's the day of the week? ")
# if day != "Saturday" or day != "Sunday":
#     print("It's not the weekend yet!")
# else:
#     print("It's the weekend!")
# --------------------------------------------------------------------

# # Task 9: Not the Correct Password (NOT)
# Create a program that prompts for a password. If the entered password
# is not "Python123", the program should display "Access Denied."

# 1. Prompt the user for a password.
# 2. Using the 'not' operator, check if the password is not "Python123".
# 3. If true, display "Access Denied."

# user_pass = input("What's the password?")
# if user_pass != "Python123":
#     print("Access denied")
# else:
#     print("Access granted.")
# --------------------------------------------------------------------

# # Task 10: What do you want to eat? (AND, NOT)
# Create a program that asks the user what they want to eat

# 1. Ask the user if they want a burger
# 2. Ask the user if they want a drink
# 3. Ask the user if they want fries
# 4. If the user wants a burger and fries but not a drink:
#     print "Won't you get thirsty?"
# burger = input("Do you want a burger?")
# drink = input("Do you want a drink?")
# fries = input("Do you want fries?")

# if burger == "Yes" and fries == "Yes" and drink == "No":
#     print(Won't you get thirsty)
# --------------------------------------------------------------------

# # Task 11: Login Credentials (AND, OR)
# Create a program that allows John to log in to TokTik.

# 1. John's username is 'John123' and his password is 'pw123'
# 2. The TokTik program will only allow John to log in.
# 3. Create 2 variables to store John's username and password
# 4. Ask John to enter his username and password
# 5. If both the username and password matches:
#     print "Access Granted"
# 6. If either the username or password is incorrect:
#     print "Either username or password is incorrect"
# 7. Otherwise:
#     print "Access Denied" 

# user = Jhon123
# pass = pw123
# input_user = input("What's the username? ")
# input_pass = input("What's the password? ")
# if input_user == user and input_pass == pass:
#     print("Access granted")
# elif input_user != user or input_pass != pass:
#     print("Either password and username is WRONG! Are you a hacker!?")
# else:
#     print("Access denied.")
# --------------------------------------------------------------------

# # Task 12: Game status report (OR, NOT)
# Imagine you're programming a simple game. Write a conditional
# statement that checks whether a variable 'game_status' is either
# "active" or not "paused". Depending on the condition, print
# appropriate messages: "Game in progress..." or "Game is paused or
# inactive."

# 1. Declare a variable game_status and assign it a value
#    (e.g. "active").
# 2. Use an 'if' statement to check if 'game_status' equals "active"
#    OR if it's NOT equal to "paused" using the 'or' and 'not'
#    logical operator.
# 3. If the condition is 'True', print "Game in progress...".
# 4. Otherwise, print "Game is paused or inactive."

game_status = input("Enter game status.")
if game_status == "active" or game_status != "pause":
    print("Game in progress.")
else:
    print("Game is paused or inactive.")
