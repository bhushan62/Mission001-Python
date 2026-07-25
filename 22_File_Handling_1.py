orders = {
    101: {
        "customer": "Bhushan",
        "service": "Dry Cleaning",
        "amount": 1350
    },
    102: {
        "customer": "Ravi",
        "service": "Wash & Iron",
        "amount": 750
    }
}

# 1. Print Bhushan's service
print(orders[101]["service"])

# 2. Change Ravi's amount to 850
orders[102]["amount"] = 850

# 3. Add status to bill number 102
orders[102]["status"] = "Ready"

# 4. Print all bill numbers and customer names
for bill_no, details in orders.items():
    print("Bill Number:", bill_no)
    print("Customer:", details["customer"])

with open("customer.txt", "w") as file:
    file.write("Customer: Bhushan\n")
    file.write("Service: Dry Cleaning\n")
    file.write("Amount: 1350\n")
    file.write("Status: Ready\n")

with open("customer.txt", "r") as file:
    for line in file:
        print(line.strip())