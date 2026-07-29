#MEMORY RULE:
# encapsulation = keep data and related methods together
# _amount       = internal-use attribute
# update method = controlled way to change data

# Create a class named LaundryOrder
class LaundryOrder:

    # Run automatically when an object is created
    def __init__(self, customer, amount):

        # Store the customer name
        self.customer = customer

        # Store the amount as an internal attribute
        self._amount = amount


    # Create a method to display the order amount
    def show_amount(self):

        # Print the current amount
        print("Amount:", self._amount)


    # Create a method to update the amount safely
    def update_amount(self, new_amount):

        # Check whether the new amount is valid
        if new_amount > 0:

            # Update the amount when the value is valid
            self._amount = new_amount

            # Show a confirmation message
            print("Amount updated successfully")

        # Run when the new amount is invalid
        else:

            # Show an error message
            print("Amount must be greater than zero")


# Create an order object
order_one = LaundryOrder("Bhushan", 1350)

# Display the original amount
order_one.show_amount()

# Update the amount using the method
order_one.update_amount(1500)

# Display the updated amount
order_one.show_amount()

# Try to update the amount with an invalid value
order_one.update_amount(-500)

# Display the amount again
order_one.show_amount()