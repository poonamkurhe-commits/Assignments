health=int(input("Enter health :"))
weapon=input("Do you have weapon?(yes/no) :")
if health>=50:
    if weapon=="yes":
        print("Zombie Defeated")
    else:
        print("Run Away")
else:
    print("Game over")