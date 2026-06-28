# Question 2: ATM Transaction Counter
# Description: Given N transactions, count how many are deposits and withdrawals.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
n = int(input("Enter number of transactions: "))
deposit = 0
withdraw = 0
for i in range(n):
    t = input("Enter transaction (D/W): ")
    if t == "D":
        deposit += 1
    elif t == "W":
        withdraw += 1
print("Deposits =", deposit)
print("Withdrawals =", withdraw)