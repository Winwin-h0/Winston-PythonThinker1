# print("Hello from lesson 4")
# # Lesson 4 - Strings

# ## Recap 1: Sushi Checkout

# You just had a lunch at a sushi restaurant and have to
# calculate the total amount you have spent. Different coloured
# plates costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3


# You have ordered a total of 3 red plates, 5 blue plates, and 4
# green plates.

# Calculate and print the total amount you have spent: -->

# red_price = 1
# blue_price = 2
# green_price = 3
# num_red = 3
# num_blue = 5
# num_green = 4
# # total = (red_price * num_red) + (blue_price * num_blue) + (green_price * num_green)
# total = red_price * num_red + blue_price * num_blue + green_price * num_green

# print(total)

# username = input("What is your username?")
# print(username)


# ---------------------------------------------------------------

# ## Task 1: Storing and printing Strings

# **Task 1a**:
# Use the input() function to ask the user for their name and
# store it in a variable. Then print that variable.

# name = input("what is your name? ")
# print(" Hi, " + (name) + "!")

# **Task 1b**:
# Ask the user for their favorite colour using input() and
# store the response in a variable. Print the variable.


# colour = input("what is your favourite colour? ")
# print(colour)

# **Task 1c**:
# Ask the user for their age using input() and store the answer
# in a variable. Print the variable.

# age = input("what is your age? ")
# print(age)
# ---------------------------------------------------------------

# ## Task 2: Input & string concatenation

# **Task 2a**:
# Ask the user for their name using input() and store it in a
# variable. 
# Concatenate the name with "Hi, [name]!" and print the
# complete message.

# name = input("what is your name? ")
# print("Hi, " + name + "!")


# **Task 2b**:
# Use input() to ask the user for their favorite hobby. Store this
# in a variable.
# Print a message saying "I enjoy [hobby]" using string
# concatenation.
# hobby = input("what is your favourite hobby?")
# print("I enjoy " + hobby)
# **Task 2c**:
# Ask the user for their dream vacation destination using input()
# and store it in a variable.
# Concatenate this variable with a phrase like "I would love to
# visit" and print the full sentence.

# dream_vacation = input("where is your dream vacation destination?: ")
# print("I would love to visit " + dream_vacation)
# ---------------------------------------------------------------

# ## Task 3: Type conversion, math, and string concatenation

# **Task 3a**:
# 1. Ask the user for their current age using input(). Convert this
# to an integer.
# 2. Add 1 to their age and convert it back to a string.
# 3. Then print a message saying "Next year, you will be [age+1]
# years old."

# current_age = input("what is your current age? ")
# next_year_age = int(current_age) + 1
# print("next year you will be " + str(next_year_age) + " years old")


# **Task 3b**:
# 1. Use input() to ask the user for a number. Convert this number
# from a string to an integer.
# 2. Double the number and convert it back to a string.
# 3. Print "Double your number is [double the number]".

# number = input("give me a number ")
# new_num = int(number) * 2
# print("double your number is " + str(new_num))


# **Task 3c**:
# 1. Use input() to ask the user for the year they were born and
# convert it to an integer.
# 2. Subtract the birth year from the current year (assume the
# current year as an integer) to find their age.
# 3. Convert the age back to a string and print "You are [age]
# years old".

# year = input("what year were you born? ")
# year_new = 2026 - int(year)
# print("you are " + str(year_new) + " years old")



# ---------------------------------------------------------------

# ## Task 4: Variable Reassignment Basics

# Assign the string "Hello" to a variable 'message'. 

message = "Hello"
message = 10
print(message)# Then reassign 'message' to the integer "10" and print it.

# ---------------------------------------------------------------

# ## Task 5: Printing Full Name


# Create 2 variables, 'firstName' and 'lastName', assigning your
# first and last names to them. Then print them on the same line
# with a space between them.
first_name = "winston"
last_name = "ho"
print(first_name  + " " + last_name)
# ---------------------------------------------------------------

# ## Task 6: Age and Name Concatenation

# Assign a name to the variable "user_name"
# Assign an integer to the variable "user_age"
# Use type conversion and string concatenation to print out
# "[user_name] is [user_age] years old."

user_name = "winston"
user_age = 9
print(user_name + " is " + str(user_age) + " years old")

print(type("1.0"))
print(type(1.0))
print(type(1))