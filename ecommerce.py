"""
System imitating Ecommerce System
"""
import logging
import pdb

# Configure logging
logging.basicConfig(filename="ecommerce_logs.log", level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")


class Product:
    """
    Represents a product with a name, price, and quantity.

    Attributes
    ----------
    name : str
        The name of the product.
    price : float
        The price of the product.
    quantity : int
        The quantity of the product.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        """
        Calculates the total price of the product based on its price
        and quantity.

        Returns
        -------
        float
            The total price.
        """
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        """
        Updates the quantity of the product.

        Parameters
        ----------
        new_quantity : int
            The new quantity value.
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            logging.error(f"Invalid quantity value {new_quantity}. \
                          Quantity cannot be negative.")


class ShoppingCart:
    """
    Represents a shopping cart containing products.

    Attributes
    ----------
    products : dict
        Dictionary containing products and their quantities in the cart.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        """
        Adds a product to the shopping cart.

        Parameters
        ----------
        product : Product
            The product to add.
        quantity : int
            The quantity of the product to add.
        """
        if quantity <= 0:
            logging.error(f"Invalid quantity value {quantity}. \
                          Quantity must be greater than zero.")
            return

        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        """
        Removes a product from the shopping cart.

        Parameters
        ----------
        product : Product
            The product to remove.
        quantity : int
            The quantity of the product to remove.
        """
        if product in self.products:
            if self.products[product] <= quantity:
                del self.products[product]
            else:
                self.products[product] -= quantity
        else:
            logging.error(f"{product.name} not found in the cart.")

    def get_total_cart_price(self):
        """
        Calculates the total price of all products in the shopping cart.

        Returns
        -------
        float
            The total price of the shopping cart.
        """
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_total_price() * quantity
        return total_price


class Customer:
    """
    Represents a customer with a name, email, and shopping cart.

    Attributes
    ----------
    name : str
        The name of the customer.
    email : str
        The email address of the customer.
    shopping_cart : ShoppingCart
        The shopping cart of the customer.
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        """
        Adds a product to the customer's shopping cart.

        Parameters
        ----------
        product : Product
            The product to add.
        quantity : int
            The quantity of the product to add.
        """
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        """
        Removes a product from the customer's shopping cart.

        Parameters
        ----------
        product : Product
            The product to remove.
        quantity : int
            The quantity of the product to remove.
        """
        self.shopping_cart.remove_product(product, quantity)

    def checkout(self):
        """
        Processes the checkout by displaying the total price
        and clearing the shopping cart.
        """
        total_price = self.shopping_cart.get_total_cart_price()
        if total_price > 0:
            print(f"Checking out... Your total is ${total_price}.")
            self.shopping_cart.products = {}
        else:
            print("Your cart is empty. Nothing to checkout.")


# Test the e-commerce system
product1 = Product("Keyboard", 50, 2)
product2 = Product("Mouse", 30, 3)

customer = Customer("John Doe", "john.doe@example.com")

# Start debugging with pdb
pdb.set_trace()

customer.add_to_cart(product1, 1)
customer.add_to_cart(product2, 2)
customer.checkout()

try:
    customer.add_to_cart(product1, -1)  # This should log an error
except ValueError as e:
    print(e)

try:
    customer.remove_from_cart(product2, 3)  # This should log an error
except ValueError as e:
    print(e)
