# Question 3: Bus Seat Checker
# Description: Print all available seat numbers from 1 to N excluding reserved seats.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
n = int(input("Enter total number of seats: "))
r = int(input("Enter number of reserved seats: "))
reserved = []
for i in range(r):
    seat = int(input("Enter reserved seat number: "))
    reserved.append(seat)
print("Available seats are:")
for i in range(1, n + 1):
    if i not in reserved:
        print(i)