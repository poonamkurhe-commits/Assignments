# Question 9: Shopping Discount
# Description: Calculate discounted price.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))
result = calculate_discount(price, discount)
print("Discounted Price =", result)