# Question 10: Delivery Charge
# Description: Return delivery charge based on order amount.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
def delivery_charge(amount):
    if amount >= 500:
        return 0
    else:
        return 50
amount=float(input("Enter order amount: "))
charge=delivery_charge(amount)
print("Delivery Charge =",charge)