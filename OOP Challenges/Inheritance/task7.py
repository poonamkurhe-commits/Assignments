# Task 7: Multi-Role Employee System (Multilevel Inheritance)
# Implement three classes: Person (attributes: name), Employee (inherits from Person, adds emp_id), and
# Manager (inherits from Employee, adds department). Ensure proper constructor chaining using
# super().
# EXAMPLE INPUT
# mgr = Manager("Rohan", "E101", "AI Ops")
# print(f"{mgr.name} | {mgr.emp_id} | {mgr.department}")
# EXPECTED OUTPUT
# Rohan | E101 | AI Ops
class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
        
class Manager(Employee):
    def __init__(self,name,emp_id,department):
        super().__init__(name,emp_id)
        self.department=department

mgr = Manager("Rohan", "E101", "AI Ops")
print(f"{mgr.name} | {mgr.emp_id} | {mgr.department}")