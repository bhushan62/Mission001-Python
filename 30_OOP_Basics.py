  # Memory Rule

# class      = blueprint
# object     = actual item
# __init__   = automatic setup
# self       = current object
# method     = function inside a class





# Create a class named LaundryOrder
class LaundryOrder:

    # This method runs automatically when an object is created
    def __init__(self, customer, service, amount):                                                                # __init__() runs automatically when an object is created.

        # Store the customer name inside the object
        self.customer = customer                                                                                  # self means the current object.

        # Store the service name inside the object
        self.service = service

        # Store the order amount inside the object
        self.amount = amount


    # Create a method to display order details
    def show_order(self):                                                              

        # Print the customer name
        print("Customer:", self.customer)

        # Print the service name
        print("Service:", self.service)

        # Print the amount
        print("Amount:", self.amount)


# Create the first order object
order_one = LaundryOrder("Bhushan", "Dry Cleaning", 1350)

# Create the second order object
order_two = LaundryOrder("Ravi", "Wash and Iron", 750)

# Display the first order
order_one.show_order()

# Print a separator line
print("--------------------")

# Display the second order
order_two.show_order()

# Create a class named LaundryOrder
class LaundryOrder:

    # This method runs automatically when an object is created
    def __init__(self, customer, service, amount):

        # Store the customer name
        self.customer = customer

        # Store the service name
        self.service = service

        # Store the order amount
        self.amount = amount

        # Give every new order a starting status
        self.status = "Processing"


    # Create a method to display all order details
    def show_order(self):

        # Print the customer name
        print("Customer:", self.customer)

        # Print the service name
        print("Service:", self.service)

        # Print the amount
        print("Amount:", self.amount)

        # Print the current order status
        print("Status:", self.status)


    # Create a method to change the order status
    def update_status(self, new_status):

        # Replace the old status with the new status
        self.status = new_status


# Create the first order object
order_one = LaundryOrder("Bhushan", "Dry Cleaning", 1350)

# Display the order before changing the status
order_one.show_order()

# Print a separator line
print("--------------------")

# Change the order status from Processing to Ready
order_one.update_status("Ready")

# Display the order after changing the status
order_one.show_order()