# Ask the user to enter the first number
number_one = int(input("Enter first number: "))

# Ask the user to enter the second number
number_two = int(input("Enter second number: "))


# Start the block that may create an error
try:

    # Divide the first number by the second number
    result = number_one / number_two

    # Print the answer if no error occurs
    print("Result:", result)


# Handle the error caused by dividing by zero
except ZeroDivisionError:

    # Show a clear message instead of stopping the program
    print("You cannot divide a number by zero")