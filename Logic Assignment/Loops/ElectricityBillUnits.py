# Question 5: Electricity Bill Units
# Description: Count how many days crossed a given unit threshold.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
n = int(input("Enter number of days: "))
threshold = int(input("Enter unit threshold: "))
count = 0
for i in range(1, n + 1):
    units = int(input(f"Enter units consumed on Day {i}: "))
    if units > threshold:
        count += 1
print("Number of days crossed threshold =", count)