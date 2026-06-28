# Question 4: Temperature Analyzer
# Description: Find the highest temperature recorded in a week.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
highest = float(input("Enter temperature for Day 1: "))
for i in range(2, 8):
    temp = float(input(f"Enter temperature for Day {i}: "))
    if temp > highest:
        highest = temp
print("Highest temperature =", highest)