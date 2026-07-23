number = int(input("Enter Number: "))

original = number
temp = number

count = 0

# Count the digits
while temp > 0:
    count = count + 1
    temp = temp // 10

temp = number
total = 0

# Armstrong calculation
while temp > 0:
    digit = temp % 10
    total = total + (digit ** count)
    temp = temp // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")