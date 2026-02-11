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

name = input("What is your name? ")
repeat = int(input("How many times to repeat? "))
for i in range(repeat):
    print("nice to meet you, " + name)

# find the sum of 3 + 8 + 13 + 18 + ... + 48
sum = 0
for i in range(3, 49, 5):
    sum += i
print(sum)



