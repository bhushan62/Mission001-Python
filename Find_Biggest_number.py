num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 > num2 and num1 > num3:
    print("a is bigger")
elif num2 > num1 and num2 > num3:
    print("b is bigger")
elif num3 > num2 and num3 > num1:
    print("c is bigger")
else:
    print("all numbers given are same")
