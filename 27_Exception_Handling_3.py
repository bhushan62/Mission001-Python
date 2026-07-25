# try     = test the code
# except  = handle the error
# else    = run when there is no error
# finally = run every time


# Start a block that may create an error
try:

    # Ask the user to enter the first number
    number_one = int(input("Enter first number: "))

    # Ask the user to enter the second number
    number_two = int(input("Enter second number: "))

    # Divide the first number by the second number
    result = number_one / number_two


# Run this block when the user enters text instead of a number
except ValueError:

    # Show a clear message
    print("Please enter numbers only")


# Run this block when the second number is zero
except ZeroDivisionError:

    # Show a clear message
    print("You cannot divide by zero")


# Run this block only when no error happens
else:

    # Print the result
    print("Result:", result)


# Run this block whether an error happens or not
finally:

    # Show that the program has finished
    print("Program completed")