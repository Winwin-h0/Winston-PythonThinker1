"""
============================================================
Q1. Bill Splitter
============================================================
You are making a simple bill-splitting calculator for a group of friends.
The program must ask for the total bill amount and how many people are sharing the bill.
It should calculate how much each person pays (equal split).

Program Requirements:
- Ask the user for Total bill
- Ask the user for Number of people
- Calculate how much each person pays
- Print the result exactly in this format:
    Each person pays: $<amount>

Note:
- The output must be rounded to 2 decimal places (example: $25.25).
- Follow the input order exactly as shown in the Test Cases.
- You must get the correct output for ALL 3 test cases.

============================================================
"""

# ============================================================
# Step 1: Ask for Total Bill
# ============================================================
total_bill = int(input("What is the total bill? "))


# ============================================================
# Step 2: Ask for Number of People
# ============================================================
num_of_people = int(input("How many people? "))


# ============================================================
# Step 3: Calculate Equal Split
# ============================================================
# - Divide total bill by number of people
# - Store result in a variable
# ============================================================
equal_split = total_bill / num_of_people


# ============================================================
# Step 4: Print Final Result
# ============================================================
# - Print the result in this format:
#   Each person pays: $<amount>
#   Rounded to 2 decimal places
# ============================================================
amount = round((equal_split), 2)
print("Each person pays: $" + str(amount))