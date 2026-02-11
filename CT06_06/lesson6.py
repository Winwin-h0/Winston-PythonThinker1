print("Hello from lesson 6")
# # Lesson 6 - Debugging

# ## Recap 1: Class Average Calculator

# You have been tasked to create a programme that calculates the
# average marks of a class.

# Your programme will have to ask the
# user for the total number of students, followed by the marks of
# each student one at a time.

# Use only variables, math operators that you have learnt, as
# well as a 'for' loop.

# sum = 0
# num_of_students = int(input("What is the total number of students? "))
# for i in range(num_of_students):
#     score_of_students = int(input("what is the score of a student? "))
#     sum = sum + score_of_students
# average = sum / num_of_students
# print(average)


# ---------------------------------------------------------------

# ## Task 1: Syntax Errors
# Fix the errors in the following:

# **Task 1a**:
# for i in range(3)
#     print("Hello, World!")

# for i in range(3):
#     print("Hello, World!")

# **Task 1b**:
# for i in range(5):
# print(i)

# for i in range(5):
#     print(i)

# **Task 1c**:
# print("Hello, World!)

# **Task 1c**:
# print("Hello, World!")

# **Task 1d**:
# if = 5

# name = 5
    
# **Task 1e**:
# print "Hello, World!"

# print ("Hello, World!")
# ---------------------------------------------------------------

# ## Task 2: Name Errors
# Fix the errors in the following:

# **Task 2a**:
# print(age)
# age = 2
# print(age)

# **Task 2b**:
# name = "Alice"
# print(nam)

# name = "Alice"
# print(name)

# **Task 2c**:
# print(x)
# x = 5

# x = 5
# print(x)

# **Task 2d**:
# pint("Hello, World!")

# print("Hello, World!")

# ---------------------------------------------------------------

# ## Task 3: Type Errors
# Fix the errors in the following:

# **Task 3a**:
# age = "25"
# print(age + 1)

# age = 25
# print(age + 1)

# **Task 3b**:
# number = 10
# print(number - "5")

# number = 10
# print(number - int("5"))

# **Task 3c**:
# print("Repeat" * "3")

# print("Repeat" * int("3"))

# **Task 3d**:
# year = 2023
# print("The year is " + year)

# year = str(2023)
# print("The year is " + year)

# **Task 3e**:
# x = "10"
# y = x / 2

# x = int("10")
# y = x / 2

# **Task 3f**:
# end = "5"
# for i in range(end):
#     print(i)

# end = int("5")
# for i in range(end):
#     print(i)


# Q1.
# This code is supposed to find the sum of numbers from 1 to 5.
# 1 + 2 + 3 + 4 + 5 = 15

# total = 0
# for i in range(1, 5):
#     total += i
# print(total)

# total = total + 5
# total += 5 

# What is wrong?
# A. The loop stops too early
# B. total should start from 1
# C. += is incorrect
# D. print is in the wrong place

# Ans: A

# Q2.
# This code is supposed to add all numbers from 1 to 5.

# for i in range(1, 6):
#     total = 0
#     total += i
# print(total)

# What is the main problem?
# A. i should start from 0
# B. range(1, 6) is incorrect
# C. total is reset every loop
# D. print should be inside the loop

# Ans: C

# Q3.
# This code is supposed to add all numbers from 0 to 4 into total.

# total = 0
# for i in range(5):
#     i += total #  i = i + total
# print(total)

# Why does total stay 0?
# A. total is never updated
# B. the loop does not run
# C. range(5) is wrong
# D. i cannot change

# Ans: A

# Q4.
# This code is supposed to find the sum of odd numbers from 1 to 9.
# 1 + 3 + 5 + 7 + 9 = 25

# total = 0
# for i in range(1, 10, 2):
#     total += 2  #total = total + 2
# print(total)
# i = 1
# total = total + 2 = 2
# i = 3
# total = total + 2 = 4
# i = 5
# total = total + 2 = 6
# i = 7
# total = total + 2 = 8
# i = 9
# total = total + 2 = 10
# i = 11
# out of loop
# correct answer
# i = 1
# total = total + 1 = 1
# i = 3
# total = total + 3 = 4
# i = 5
# total = total + 5 = 9
# i = 7
# total = total + 7 = 16
# i = 9
# total = total + 9 = 25
# i = 11
# out of loop

# What is the mistake?
# A. The wrong value is added
# B. The range is incorrect
# C. total should start from 1
# D. The step size is wrong

# Ans: A

# total = 0
# for i in range(1, 10, 2):
#     total += i  #total = total + i
# print(total)

# Q5.
# This code is supposed to find the sum of numbers from 1 to 5.
# 1 + 2 + 3 +4 + 5
total = 0
for i in range(1, 6):
    total += 1
# i = 1: total = total + 1 = 1
# i = 2: total = total + 1 = 2
# i = 3: total = total + 1 = 3
# i = 4: total = total + 1 = 4
# i = 5: total = total + 1 = 5

print(total)

# What is the code actually doing?
# A. Counting how many times the loop runs
# B. Adding numbers from 1 to 5
# C. Adding only the last number
# D. Nothing

# Ans: A
# for i in range(1, 6):
#     total += i
# print(total)

# Q6.
# This code is supposed to find the sum of numbers from 1 to 5.

# total = 0
# for i in range(1, 6):
#     total = i
# print(total)

# Why is the answer wrong?
# A. total is overwritten each loop
# B. range(1, 6) is incorrect
# C. i should start from 0
# D. print should be inside the loop

# Ans: A

# This code is supposed to print the sum of numbers from 10 to 1
# (10 + 9 + 8 + ... + 1 = 55).

# total = 0
# for i in range(10, 0):
#     total += i 
# print(total)


# total = 0
# for i in range(10, 0, -1):
#     total += i 
# print(total)

# This code is supposed to print:
# • the sum of numbers from 1 to 5 (15)
# • the sum of numbers from 6 to 10 (40)
# 15 40

# total1 = 0
# total2 = 0

# for i in range(1, 6):
#     total2 += i

# for i in range(6, 11):
#     total1 += i

# print(total1, total2)


# total1 = 0
# total2 = 0

# for i in range(1, 6):
#     total1 += i

# for i in range(6, 11):
#     total2 += i

# print(total1, total2)

# This code is supposed to print the sum of numbers from 1 to n.
# If n = 6, it should print 21.
# 1 + 2 + 3 + 4 +5 +6

# n = 6
# total = 0
# for i in range(1, n + 1):
#     total += i #total = total + n
# print(total)

# This code is supposed to print the sum of even numbers from 2 to 20 (110).
# 2 + 4 + 6 + ... +18 + 20
# total = 0
# for i in range(2, 21, 2):
#     total += i
# print(total)


# Q7. (Logic Error – end value missing)
# This code is supposed to print the sum of multiples of 3 from 3 to 30 (165).
total = 0
for i in range(3, 31, 3):
    total += i
print(total)