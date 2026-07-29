# Store the name of the text file in a variable
file_name = "laundry_order.txt"


# Open the file in write mode
# "w" creates a new file or removes the old content
with open(file_name, "w") as file:

    # Write the customer name into the file
    file.write("Customer: Ravi\n")

    # Write the service name into the file
    file.write("Service: Wash and Iron\n")

    # Write the order amount into the file
    file.write("Amount: 750\n")


# Open the same file in append mode
# "a" keeps the old content and adds new content at the end
with open(file_name, "a") as file:

    # Add the order status to the file
    file.write("Status: Processing\n")


# Open the same file in read mode
# "r" reads the content without changing it
with open(file_name, "r") as file:

    # Read the complete file and store it in the variable named content
    content = file.read()


# Print the saved content in the terminal
print(content)