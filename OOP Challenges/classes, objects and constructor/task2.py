# Task 2: Student Grading System
# Create a Student class initialized with name and a list of marks. Implement a method get_grade() that
# calculates the average marks and returns "A" (>=90), "B" (>=75 and <90), "C" (>=50 and <75), or "F"
# (<50).
# EXAMPLE INPUT
# s1 = Student("Rahul", [85, 90, 78, 92])
# print(s1.get_grade())
# EXPECTED OUTPUT
# B
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"
s1 = Student("Rahul", [85, 90, 78, 92])
print(s1.get_grade())