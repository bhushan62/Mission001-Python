num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))
num3 = int(input("Enter Third Number"))

if num1 < num2 and num1 < num3:
    print("Number 1 is smaller")
elif num2 < num1 and num2 < num3:
    print("Number 2 is smaller")
elif num3 < num1 and num3 < num2:
    print("Number 3 is smaller")

elif num1 == num2 == num3:
    print("All are same")