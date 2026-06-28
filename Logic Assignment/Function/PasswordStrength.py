# Question 8: Password Strength
# Description: Function returns whether password length is acceptable.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
def check_password(password):
    if len(password) >= 8:
        return "Password is Strong"
    else:
        return "Password is Weak"
password=input("Enter password: ")
result=check_password(password)
print(result)