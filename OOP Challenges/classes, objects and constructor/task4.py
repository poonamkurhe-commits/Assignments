# Task 4: Bank Account State
# Design a BankAccount class with account_holder and balance. Implement deposit(amount) and
# withdraw(amount). Ensure that a user cannot withdraw more money than the current balance.
# EXAMPLE INPUT
# acc = BankAccount("Amit", 1000)
# acc.deposit(500)
# acc.withdraw(2000)
# print(acc.balance)
# EXPECTED OUTPUT
# Insufficient Balance
# 1500
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")
acc = BankAccount("Amit", 1000)
acc.deposit(500)
acc.withdraw(2000)
print(acc.balance)