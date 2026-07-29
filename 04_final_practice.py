# This program combines:

# Class
# Object
# __init__()
# Methods
# Multiple objects
# Inheritance
# super()
# Encapsulation-style controlled updates


# Create the parent class
class LaundryOrder:

    # Run automatically when an order object is created
    def __init__(self, customer, service, amount):

        # Store the customer name
        self.customer = customer

        # Store the service name
        self.service = service

        # Store the amount as an internal attribute
        self._amount = amount

        # Give every new order a default status
        self.status = "Processing"


    # Create a method to display order details
    def show_order(self):

        # Print the customer name
        print("Customer:", self.customer)

        # Print the service name
        print("Service:", self.service)

        # Print the amount
        print("Amount:", self._amount)

        # Print the current status
        print("Status:", self.status)


    # Create a method to update the order amount
    def update_amount(self, new_amount):

        # Check whether the new amount is valid
        if new_amount > 0:

            # Replace the old amount
            self._amount = new_amount

            # Show confirmation
            print("Amount updated successfully")

        # Run when the amount is invalid
        else:

            # Show an error message
            print("Amount must be greater than zero")


    # Create a method to update the order status
    def update_status(self, new_status):

        # Replace the old status
        self.status = new_status


# Create a child class for express orders
class ExpressOrder(LaundryOrder):

    # Run automatically when an express order is created
    def __init__(self, customer, service, amount, delivery_hours):

        # Call the parent class constructor
        super().__init__(customer, service, amount)

        # Store the delivery time
        self.delivery_hours = delivery_hours


    # Create a method to display express-order details
    def show_express_order(self):

        # Reuse the parent class display method
        self.show_order()

        # Print the express delivery time
        print("Delivery time:", self.delivery_hours, "hours")


# Create a normal order object
normal_order = LaundryOrder(
    "Bhushan",
    "Dry Cleaning",
    1350
)

# Create an express order object
express_order = ExpressOrder(
    "Ravi",
    "Wash and Iron",
    1800,
    24
)

# Display the normal order
print("NORMAL ORDER")
normal_order.show_order()

# Print a separator
print("--------------------")

# Update the normal order amount
normal_order.update_amount(1500)

# Update the normal order status
normal_order.update_status("Ready")

# Display the updated normal order
normal_order.show_order()

# Print another separator
print("--------------------")

# Display the express order
print("EXPRESS ORDER")
express_order.show_express_order()