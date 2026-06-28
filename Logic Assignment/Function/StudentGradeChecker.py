# Question 7: Student Grade Checker
# Description: Return grade based on marks.
# Input: Define suitable input.
# Output: Produce the required result.
# Constraint: Use the topic concepts properly and write clean logic
def check_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

marks = int(input("Enter marks: "))
grade = check_grade(marks)
print("Grade =", grade)