age=int(input("Enter age :"))
fitness=input("Fit?(yes/no) :")
if age>=18:
    if fitness=="yes":
        print("Mission Accepteed")
    else:
        print("Fitness Test Failed")
else:
    print("Too Young")
