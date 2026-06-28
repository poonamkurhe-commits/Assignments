key=input("Do you have key?(yes/no) :")
password=input("Enter password :")
if key=="yes":
    if password=="magic123":
        print("Access Granted")
    else:
        print("Wrong Password")
else:
    print("Key Missing")