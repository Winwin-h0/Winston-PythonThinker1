# # Lesson 8 - Importing Libraries, Boolean & Conditions

# ## Recap 1: Product of 5 numbers

# Write a program to calculate the product (multiplication) of 5
# numbers.

# 1. Using a for loop, ask the user for 5 numbers one at a time.
# 2. Calculate the multiplication for these 5 numbers and print
#    it out.
# total = 1
# for i in range(1, 6):
#     num = int(input("give me number #" + str(i) + ": "))
#     total *= num
# print("The total product is " + str(total))
# ---------------------------------------------------------------

# ## Task 1: 'time' library

# **Task 1a**:
# Import the 'time' library and make use of the 'time.sleep()'
# function to create a 10 seconds countdown timer that counts
# to 1, printing the number of seconds remaining every second.

import time

# for i in range(10, 0 , -1):
#     print(str(i) + " secounds remaining")
#     time.sleep(1)
# print("Time ended")


# **Task 1b**:
# Modify your code from Task 1a to include an 'input()' function
# asking the user for the number to countdown from, before
# counting down every second from the number given by the user.
# time_to_count = int(input("How many secounds to count down? "))

# for i in range(time_to_count, 0 , -1):
#     print(str(i) + " secounds remaining")
#     time.sleep(1)
# print("Time ended")

# ---------------------------------------------------------------

# ## Task 2: 'random' library

# **Task 2a**:
# Import the 'random' library and create a program that randomly
# output a number between 1 to 6

import random

# random_num = random.randint(1,6)
# print(random_num)

# **Task 2b**:
# Using the 'random' library, create 20 numbers between 0 and
# 9999 randomly.

# for i in range(20):
#     print(random.randint(0, 9999))
# ---------------------------------------------------------------

# ## Task 3: Print Boolean Value & Condition

# **Task 3a**:
# Assign a boolean value to a variable and print it.

bool_var = True
print(bool_var)

# **Task 3b**:
# Create 2 variables both holding the "True" boolean.
# Print out the result of comparing the 2 variables using
# the "==" operator.

bool_var1 = True
bool_var2 = True
print(bool_var1 == bool_var2)

# **Task 3c**:
# Now, assign 1 variable the "True" boolean, and assign another
# variable the "False" boolean.

# Print out the result of comparing the 2 variables using
# the "==" operator.

bool_var2 =False
bool_var1 = True
print(bool_var1 == bool_var2)

# ---------------------------------------------------------------

# ## Task 4:

# **Task 4a**: Math Question Generator
# Using the 'random' library, generate 2 numbers between 1 and 50
# that the user must add together.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# Example:
# What is 2 + 5? << 7 >>
# True
import random
# num1 = int(input("give me a number between 1 and 50 "))
# num2 = int(input("give me a number between 1 and 50 "))
num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
answer = num1 + num2
user = int(input("what is " + str(num1) + " + " + str(num2) + ": "))
print(answer == user)

# **Task 4b**: Range Guesser
# Create a program that generates a random number between 1 and
# 50.

# The user should input a range (two numbers: start and end).

# The program checks if the random number falls within the user's
# range.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# ---------------------------------------------------------------

# ## Task 5: Random Number Guessing Game

# Create a simple program to guess a random number:
# a. Create a variable called 'guess' and assign a number that
#    you are guessing
# b. Create a variable called 'num1' and assign a random integer
#    between 1 to 10.

# Your program will check if 'guess' is equal to 'num1'.

# The output should be one of the following:
# 1. True (If the answer is correct)
# 2. False (If the answer is wrong)

# ---------------------------------------------------------------

# ## Task 6: Random Multiplication Quiz

# You have been tasked by Ms Tan, the Math teacher to create a
# multiplication quiz.

# Create a program that generates a certain number of random
# multiplication questions.

# Each question should involve multiplying 2 random numbers
# between 1 and 10. The user should input the number of questions
# they want to attempt.

# ---------------------------------------------------------------

# ## Task 7: Even or Odd Checker

# Write a program that asks the user to enter a number. The
# program then tells the user whether the number is even
# (True) or odd (False).

# Your program needs to:
# 1. Ask user for an integer input.
# 2. Check if there is any remainder when user input is divided
#    by 2 (using '%').
# 3. Print 'True' if number is even, otherwise print 'False'.

# ---------------------------------------------------------------

# ## Task 8: Multiple Check Program

# Create a program where the user enters 2 numbers. The
# program then checks if the first number is a multiple of
# the second number.

# Your program needs to:
# 1. Get user to input 2 numbers.
# 2. Check if there is any remainder when number #1 is divided
#    by number #2
# 3. Print 'True' if number #1 is a multiple of number #2,
#    otherwise print 'False'.