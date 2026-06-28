# Question 1: Daily Sales Total
# Description: A shop records sales for N days. Find the total sales using loops only.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
n = int(input("Enter number of days: "))
total_sales = 0
for i in range(1, n + 1):
    sales = float(input(f"Enter sales for day {i}: "))
    total_sales += sales
print("Total Sales =", total_sales)