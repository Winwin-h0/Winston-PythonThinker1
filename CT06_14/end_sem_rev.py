# Qns 1 Lists

# groceries = ["apple", "banana", "coconut", "pineapple", "pear"]

# 1. Remove the item "banana" from the list.
# del(groceries[1])
# 2. After removing it, print the 2nd item in the list.
# print(groceries[1])
# 3. Add "dragon fruit" so that it appears immediately before "pineapple".
#    (You are not allowed to hardcode the index)
# index_pineapple = groceries.index("pineapple")
# print(f"index_pineapple is {index_pineapple}")
# groceries.insert(2,"dragon fruit")
# 4. Ask the user to continuously input grocery items.
#    Each item should be added to the END of the list.
#    Stop when the user types "end".

# user_input = input("Please input an item into the the shopping list. ").lower()

# while user_input != "end":
#     groceries.append(user_input)
#     user_input = input("Please input an item into the the shopping list. ")


# 5. Print all items in the list in this format:
#    1. apple
#    2. coconut
#    ...
# counter = 1
# for count in groceries:
#     print(f"{counter}. {count}")
#     counter += 1
# 6. Generate a random index based on the current list size.
#    Remove the item at the random index from the list.
# #    Print the item that was removed.
# import random
# index = random.randint(0, len(groceries))
# removed = groceries.pop(index)
# print(f"{removed} was the item removed.")
# 7. Ask the user to search for an item.

#    If found:
#    Print:
#    "[item] is found at position [index]"

#    If not found:
#    Print:
#    "[item] is not in the list"
# user_item = input("What is the item to search for? ")
# specific_item =  user_item
# if specific_item in groceries:
#     index_specific = groceries.index(specific_item)
#     print(f"{user_item} is found at {index_specific}.")
# else:
#     print(f"{specific_item} is not in the list. ")


# Qns 2 Modified If - elif - else and order of operations

# A reward system works as follows:
# 1. If the score is NOT between 0 and 100, print "Invalid score"

# 2. If the player is NOT banned AND score is above 89
#    OR the player is a member AND score is above 95,
#    print "Gold reward"

# 3. If the score is above 74 
#    print "Silver reward

# 4. Otherwise, print "Bronze reward"

# score = int(input("What is your score?"))
# banned = input("Are you banned? (y/n) ").lower()
# while banned != "y" or banned != "n":
#     print("Please input only y or n.")
#     banned = input("Are you banned? (y/n) ").lower() 

# player = input("Are you a member? (y/n) ")
# if score < 0 or score > 100:
#     print("Invalid score")
# elif (banned == "n" and score > 89) or (player == "y" and score > 95):
#     print("Gold reward. Keep up the good work!")
# elif score > 74:
#     print("Sliver award. Almost there. ")
# else:
#     print("Bronze reward. Try harder. ")

# Qns 2 If - elif - else and order of operations

# A reward system works as follows:

# 1. If the score is NOT between 0 and 100, print "Invalid score"
# 2. If the player is NOT banned AND score is above 89
#    OR the player is a member AND score is above 95,
#    print "Diamond reward"
# 3. If the score is above 74 AND (the player is a member OR has finished the game),
#    print "Gold reward"
# 4. If the score is above 49 AND the player is NOT banned,
#    print "Silver reward"
# 5. If the player is banned OR has NOT finished the game,
#    print "No reward"
# 6. Otherwise, print "Bronze reward"

score = int(input("What is your score? "))
game = input("have you finished the game? (y/n) ")
banned = input("Are you banned? (y/n) ").lower() 
player = input("Are you a member? (y/n) ")
if banned == "y" and game == "n":
    print("No reward. You were banned and did not fininsh the game!")
elif score < 0 or score > 100:
    print("Invalid score")
elif (banned == "n" and score > 89) or (player == "y" and score > 95):
    print("Diamond reward. Superb!")
elif (score > 74 and player == "y") or (score > 74 and game == "y"):
    print("Gold award. Keep Trying! ")
elif score > 49 and banned == "n":
    print("Sliver award. Keep practicing!. ")
else:
    print("Bronze award. Don't give up!")

# Ask the user for:
# - score
# - member status ("yes" / "no")
# - banned status ("yes" / "no")
# - finished game status ("yes" / "no")

# Important:
# - You must use and, or, not
# - You must use brackets where needed
# - The order of checking matters

# Test your program with:

# Case 1:
# score = 96, member = no, banned = no, finished = yes
# Expected: Diamond reward

# Case 2:
# score = 80, member = no, banned = no, finished = yes
# Expected: Gold reward

# Case 3:
# score = 80, member = no, banned = no, finished = no
# Expected: Silver reward

# Case 4:
# score = 60, member = no, banned = yes, finished = no
# Expected: No reward

# Debug the Code

# This program should:
# 1. Keep asking the user for a score
# 2. Stop when the user types "end"
# 3. Convert each valid score into an AL level
# 4. Store all AL results in a list
# 5. Print the final list
# 6. You are NOT allowed to remove any lines.
# 7. You can only MODIFY existing lines.

# al_list = []

# while True:
#     score = input("Enter score: ")

#     if score == "end":
#         break

#     if int(score) < 0 or int(score) > 100:
#         print("Invalid")

#     elif int(score) > 89:
#         al = 1
#     elif int(score) > 84:
#         al = 2
#     elif int(score) > 79:
#         al = 3
#     elif int(score) > 74:
#         al = 4
#     elif int(score) > 64:
#         al = 5
#     elif int(score) > 44:
#         al = 6
#     elif int(score) > 19:
#         al = 7
#     else:
#         al = 8

#     al_list.append(al)

# print(f"AL list: {al_list}")