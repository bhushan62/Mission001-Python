age = int(input("Enter Age: "))

if age >= 18:
    valid_license = input("Do you have a license? (yes/no): ")

    if valid_license == "yes":
        print("You can drive.")
    else:
        print("You need a driving license.")

else:
    print("You are underage.")