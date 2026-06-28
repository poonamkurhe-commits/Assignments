# Functions
# Question 6: Salary Calculator
# Description: Create a function that calculates final salary after bonus.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
def calculate_salary(salary, bonus):
    final_salary = salary + bonus
    return final_salary
salary = int(input("Enter basic salary: "))
bonus = int(input("Enter bonus amount: "))
result = calculate_salary(salary, bonus)
print("Final Salary =", result)