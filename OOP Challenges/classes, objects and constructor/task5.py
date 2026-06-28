# Task 5: Digital Wallet Ledger
# Create a Wallet class tracking balance and a list called history. Every deposit or withdrawal should
# append a string format action (e.g., "Deposited ₹500") to history. Implement a show_history()
# method.
# EXAMPLE INPUT
# w = Wallet()
# w.deposit(100)
# w.withdraw(30)
# print(w.show_history())
# EXPECTED OUTPUT
# ['Deposited ₹100', 'Withdrew ₹30']
class Wallet:
    def __init__(self):
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew ₹{amount}")
        else:
            print("Insufficient Balance")
    def show_history(self):
        return self.history
w = Wallet()
w.deposit(100)
w.withdraw(30)
print(w.show_history())