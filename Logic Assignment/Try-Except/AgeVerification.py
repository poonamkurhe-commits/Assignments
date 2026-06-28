# Question 15: Age Verification
# Description: Handle non-numeric age input.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
except ValueError:
    print("Invalid age input")