print("Hello from lesson 7")

## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))


## Task 4: Word Repetition Input Loop

# Ask the user for a word and a number n. Print the word repeated
# n times (on separate lines).

# Example:
# What word would you like to repeat? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# burger
# burger
# burger

# word = input("What word to repeat? ")
# number = int(input("how many times to repat? "))
# for i in range(number):
#     print(word)

## Task 5: Personalized Greeting Loop

# Ask for a user's name and an integer n, then print a
# personalized greeting n times.

# Example:
# What is your name? <<burger>>
# How many times would you like to repeat? << 3 >>

# output:
# Nice to meet you, burger
# Nice to meet you, burger
# Nice to meet you, burger

# name = input("What is your name? ")
# repeat = int(input("How many times to repeat? "))
# for i in range(repeat):
#     print("nice to meet you, " + name)

# # find the sum of 3 + 8 + 13 + 18 + ... + 48
# sum = 0
# for i in range(3, 49, 5):
#     sum += i
# print(sum)


# Debugging question 1
# total = 0

# for i in range(1, 4):
#     score = input("Enter score " + str(i) + ": ")
#     total = total + int(score)

# print("Total score is: " + str(total))

# Debugging question 2
# name = input("Enter your name: ")

# for i in range(5):
#     message = str(i) + ". " + name
#     print(message)

## Task 6: Sum of Five User Inputs

# Ask the user to input 5 numbers, one at a time, and print the
# sum of these numbers.

# Example:
# What is number #1? <<5>>
# What is number #2? <<2>>
# What is number #3? <<4>>
# What is number #4? <<1>>
# What is number #5? <<7>>

# output:
# Sum of the 5 numbers is 19 

# total = 0


# for i in range(1, 6):
#     number = int(input("what is number " + str(i) + "? "))
#     total += number
# print("Sum of the 5 number is " + str(total))

## Task 7: Multiplication Table Generator

# Ask the user for a number, then print the multiplication table
# for that number from 1 to 12.

# Example:
# What number for the timestable? > << 5 >>
# output:
# 5 x 1 = 5
# 5 x 2 = 10
# ....
# ..
# 5 x 12 = 60

# timestable = int(input("What number for the timestable? "))
# anwser = 0

# for i in range(1, 13):
#     anwser = timestable * i
#     print(str(timestable) + " x " + str(i) + " = " + str(anwser))
    
## Task 8: Number Pyramid Pattern

# 1. Ask the user for a number
# 2. Using the 'for' loop, print out the number like the
#    following:

# 1
# 22
# 333
# 4444
# 55555

# Hint: You can use a code like this >>> print("a" * 5)

# number = int(input("Give me a number "))

# for i in range(1, (number + 1)):
    
#     print(str(i % 10) * i)


## Task 9: Average Calculator of 5 numbers
# Ms Tan would like to calculate the average score of her 5
# students in class 6A.

# Write a program to calculate the average of 5 numbers.

# 1. Using a 'for' loop, ask the user for 5 numbers one at a
#    time.
# 2. Calculate the average for these 5 numbers and print it
#    out.

# You will need to 
# a. sum up the numbers
# b. divide the sum by the total count.

# total = 0
# students = int(input("How many students are there? "))
# for i in range(1, (students + 1)):
#     num = int(input("What is the number " + str(i) + " " ))
#     total = total + num
# print("The average score is " + str((total / students)))

# **DISCUSS with your Code Mentor and Class on how to
# calculate the average**


# (1 * 2) + (2 * 3) + (3 * 4) + (4 * 5) + ... (10 *11)

total = 0
for i in range(1, 11):
    num = i * (i + 1)
    total = total + num
print(total)

# n= 2
#  *
# *** 

# n = 3
#    * 
#   *** 
#  *****

# n = 4
#    *  = i
#   *** = i + 1
#  ***** = i + 2
# ******* = i + 3

#    *  
#   ***
#  *****
# *******

# i = 1, 1 = 1 + 2 x 0
# i = 2, 3 = 1 + 2 = 1 + 2 x 1
# i = 3, 5 = 1 + 2 + 2 = 1 + 2 x 2
# i = 4, 7 = 1 + 2 + 2 + 2 = 1 + 2 x 3
# i = 5, 9 = 1 + 2 + 2 + 2 + 2 = 1 + 2 x 4
# i = 6, 11 = 1 + 2 + 2 + 2 + 2 + 2 = 1 + 2 x 5

# 1 + 2 x (i - 1)

# n = 4
# i = 4, 0 =  n - 4
# i = 3, 1 = n - 3
# i = 2, 2 = n - 2
# i = 1, 3 = n - 1
# n - i

# " " * (n - i) + "*" * (1 + 2 * (i - 1)) + " " * (n - i)

num = int(input("Give me 'n': " ))
            
for i in range(1, (num + 1)):
    print(" " * (num - i) + "*" * (1 + 2 * (i - 1)) + " " * (num - i))


# 1) Centre-Aligned Number Pyramid (Wrap at 9)
# -------------------------------------------
# Write a program that prints a centre-aligned number pyramid of height n.

# Each row:
# - Is centred using spaces
# - Prints numbers starting from 1
# - Wraps around after 9 (e.g. 10 → 0, 11 → 1)

# Example (n = 6):
#      1
#     123
#    12345
#   1234567
#  123456789
# 12345678901

# Rules:
# - No if / else
# - Nested for loops allowed


# 5) Palindrome Number Pyramid
# ----------------------------
# Write a program that prints a centre-aligned palindrome number pyramid.

# Example (n = 4):
#    1
#   121
#  12321
# 1234321

# Rules:
# - No if / else
# - Nested for loops allowed