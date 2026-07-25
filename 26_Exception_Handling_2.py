# Start a block that may create an error
try:

    # Ask the user to enter the first number
    number_one = int(input("Enter first number: "))

    # Ask the user to enter the second number
    number_two = int(input("Enter second number: "))

    # Divide the first number by the second number
    result = number_one / number_two

    # Print the result if no error happens
    print("Result:", result)


# Runs when the user enters text instead of a number
except ValueError:

    # Show a clear message
    print("Please enter numbers only")


# Runs when the second number is zero
except ZeroDivisionError:

    # Show a clear message
    print("You cannot divide by zero")