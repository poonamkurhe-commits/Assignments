# Task 9: Bank Account Tiers (Hierarchical Inheritance)
# Create a base class Account. Derive two separate classes from it: SavingsAccount (adds
# interest_rate) and CurrentAccount (adds overdraft_limit). Both must override a base method
# account_type().
# EXAMPLE INPUT
# s = SavingsAccount()
# c = CurrentAccount()
# print(s.account_type(), "and", c.account_type())
# EXPECTED OUTPUT
# Savings Tier and Current Tier
class Account:
    def account_type(self):
        return "Account"
class SavingsAccount(Account):
    def __init__(self):
        self.interest_rate = 5
    def account_type(self):
        return "Saving Tier"
class CurrentAccount(Account):
    def __init__(self):
        self.overdraft_limit = 10000
    def account_type(self):
        return "Current Tier"
    
s = SavingsAccount()
c = CurrentAccount()
print(s.account_type(), "and", c.account_type())
