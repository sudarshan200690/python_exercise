num1 = int(input("Please enter 1st No:"))
num2 = int(input("Please enter 2nd No:"))
num3 = int(input("Please enter 3rd No:"))
if num1 >= num2 and num1 >= num3:
    print("\n" + str(num2), "is greatest number")
elif num2 >= num3:
    print("\n" + str(num2), "is greatest number")
else:
    print("\n" + str(num3), "is greatest number")