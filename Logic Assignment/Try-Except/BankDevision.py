# Question 12: Bank Division
# Description: Handle division by zero while calculating ratios.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
try:
    amount=int(input("Enter amount: "))
    people=int(input("Enter number of people: "))
    result=amount / people
    print("Ratio =", result)
except ZeroDivisionError:
    print("Cannot divide by zero")