# Question 11: Online Payment
# Description: Handle invalid payment amount input.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
try:
    amount=float(input("Enter payment amount: "))
    print("Payment Successful")
except ValueError:
    print("Invalid payment amount")