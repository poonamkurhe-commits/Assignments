fuel=int(input("Enter fuel percentage :"))
weather=input("Weather good?(yes/no) :")
if fuel>=70:
    if weather=="yes":
        print("Launch Successful")
    else:("Launch Delayed Due To Weather")
else:
    print("Not Enough Fuel")