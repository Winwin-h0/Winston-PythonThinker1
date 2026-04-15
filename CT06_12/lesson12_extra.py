# use while condition
# A1. Count from 1 to 5
# Write a program that prints the numbers 1 to 5 using a while loop.
# Prints 1, 2, 3, 4, 5 (each on a new line)
counter = 1
while counter <= 5:

    print(counter)
    counter += 1

# A2. Count from 10 down to 1
# Write a while loop that prints 10, 7 ,4, 1
# Prints numbers in descending order from 10 to 1
counter = 10
while counter >= 1:
    print(counter)
    counter -= 3

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



# while True

# C1. Password checker
# Keep asking the user to type the password "python123". Stop only when it is correct.
# Loop continues until correct password is entered
password = "python123"
# user = input("What's the password? ")
# while user != password:
#     print("wrong")
#     user = input("What's the password? ")
# else:
#     print("Correct")
# user = input("What's the password? ")
while True:
    # input is the first thing in while True
    user = input("What's the password? ")
    # next identify the exit condition
    if user == password:
        print("Correct")
        break


    
# C2. Menu exit
# Ask the user to type "play" or "quit". If they type "quit", stop the program.
# Loop only ends when "quit" is entered

while True:
    user = input("play or quit")
    if user == "quit":
        break

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