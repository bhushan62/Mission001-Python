# Create the parent class
class LaundryOrder:

    # Run automatically when an order object is created
    def __init__(self, customer, service, amount):

        # Store the customer name
        self.customer = customer

        # Store the service name
        self.service = service

        # Store the order amount
        self.amount = amount


    # Create a method to display normal order details
    def show_order(self):

        # Print the customer name
        print("Customer:", self.customer)

        # Print the service name
        print("Service:", self.service)

        # Print the amount
        print("Amount:", self.amount)


# Create a child class that inherits LaundryOrder
class ExpressOrder(LaundryOrder):

    # Run automatically when an express order is created
    def __init__(self, customer, service, amount, delivery_hours):

        # Call the parent class constructor
        super().__init__(customer, service, amount)

        # Store the express delivery time
        self.delivery_hours = delivery_hours


    # Create a method for express-order information
    def show_express_details(self):

        # Reuse the parent class method
        self.show_order()

        # Print the express delivery time
        print("Delivery time:", self.delivery_hours, "hours")


# Create an object from the child class
express_order = ExpressOrder(
    "Ravi",
    "Dry Cleaning",
    1800,
    24
)

# Display the complete express-order details
express_order.show_express_details()