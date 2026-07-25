                         #        Simple comparison
# Mode	Meaning	Existing content
# "w"	Write	Deleted and replaced
# "a"	Append	Kept; new data added
# "r"	Read	Kept; no changes



import os

file_name = "customer.txt"

# Create and write data
with open(file_name, "w") as file:
    file.write("Customer: Bhushan\n")
    file.write("Service: Dry Cleaning\n")
    file.write("Amount: 1350\n")

# Add new data
with open(file_name, "a") as file:
    file.write("Status: Ready\n")

# Check and read
if os.path.exists(file_name):
    print("File exists\n")

    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())
else:
    print("File does not exist")




