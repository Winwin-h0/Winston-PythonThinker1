# use while condition
# A1. Count from 1 to 5
# Write a program that prints the numbers 1 to 5 using a while loop.
# Prints 1, 2, 3, 4, 5 (each on a new line)

# A2. Count from 5 down to 1
# Write a while loop that prints 5, 4, 3, 2, 1.
# Prints numbers in descending order from 5 to 1


# A3
# Question:
# Write a program that starts with count = 30.
# Use a while loop to print count while:
# - count is greater than or equal to 10
# - AND count is not 18
# Each time, subtract 4 from count.
#
# Output:
# 30
# 26
# 22

# A4
# Question:
# Write a program that starts with x = 1 and total = 0.
# Use a while loop to add x into total while:
# - x is less than or equal to 8
# - AND x is not 5
# Increase x by 1 each round.
# Print total at the end.
#
# Output:
# 23

## while condition and break

# B1. Stop counting when you reach 3
# Start from 1 and count upward, but use break to stop the loop when the number becomes 3.
# Prints 1, 2, 3 and stops using break

# B2. Ask until the user types "ok"
# Use while True to keep asking for input until the user types "ok".
# Loop repeats until "ok" is entered, then stops

# B3
# Question:
# Write a program that asks the user to enter a number.
# Keep looping while the number is not 99.
# Inside the loop:
# - if the number is less than 0 OR greater than 50, print "Invalid" and break
# - otherwise print "Try again" and ask again
#
# Output:
# If user types:
# 10
# 20
# 60
#
# Output should be:
# Try again
# Try again
# Invalid

# B4
# Question:
# Write a program that checks the list:
# [5, 9, 12, 15, 18, 21]
# using a while loop and an index.
# Keep looping while the index is still inside the list.
# Inside the loop:
# - if the current number is divisible by 4 OR divisible by 7, print "Found special number" and break
# - otherwise print the number
# - move to the next index
#
# Output:
# 5
# 9
# Found special number


# while True

# C1. Password checker
# Keep asking the user to type the password "python123". Stop only when it is correct.
# Loop continues until correct password is entered

# C2. Menu exit
# Ask the user to type "play" or "quit". If they type "quit", stop the program.
# Loop only ends when "quit" is entered

# C3
# Question:
# Write a program that keeps asking the user to enter two numbers: a and b.
# Use while True.
# Break only when:
# - a is greater than b
# - AND a - b is less than 5
# If a is equal to b OR a is less than b, print "Order not correct".
# Otherwise print "Difference too big".
#
# Output:
# Example inputs:
# a = 3, b = 7
# a = 12, b = 2
# a = 9, b = 6
#
# Output:
# Order not correct
# Difference too big

# C4
# Question:
# Write a program that keeps asking the user to enter a word.
# Use while True.
# Break only when:
# - the word starts with "s"
# - AND ends with "p"
# - AND is not "stop"
# If the word is "stop" OR "skip", print "Blocked word".
# Otherwise print "Try another word".
#
# Output:
# Example inputs:
# stop
# ship
#
# Output:
# Blocked word