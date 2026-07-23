number = int(input("Enter Number: "))

count = 0

while number > 0:
    count = count + 1
    number = number // 10

print("Total Digits =", count)