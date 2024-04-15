"""
System that deals with food delivery and operations related to it
"""


class FoodItem:
    """
    Represents a food item with a name and price.

    Attributes
    ----------
    name : str
        The name of the food item.
    price : float
        The price of the food item.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    """
    Represents a restaurant with a name and menu.

    Attributes
    ----------
    name : str
        The name of the restaurant.
    menu : dict
        Dictionary containing food items and their quantities on the menu.
    """
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_to_menu(self, food_item, quantity):
        """
        Adds a food item to the restaurant's menu.

        Parameters
        ----------
        food_item : FoodItem
            The food item to add to the menu.
        quantity : int
            The quantity of the food item to add.
        """
        if food_item in self.menu:
            self.menu[food_item] += quantity
        else:
            self.menu[food_item] = quantity

    def remove_from_menu(self, food_item, quantity):
        """
        Removes a food item from the restaurant's menu.

        Parameters
        ----------
        food_item : FoodItem
            The food item to remove from the menu.
        quantity : int
            The quantity of the food item to remove.
        """
        if food_item in self.menu:
            if self.menu[food_item] <= quantity:
                del self.menu[food_item]
            else:
                self.menu[food_item] -= quantity
        else:
            print(f"{food_item.name} not found in the menu.")

    def get_total_revenue(self):
        """
        Calculates the total revenue generated from the restaurant's menu.

        Returns
        -------
        float
            The total revenue.
        """
        total_revenue = 0
        for food_item, quantity in self.menu.items():
            total_revenue += food_item.price * quantity
        return total_revenue


class Customer:
    """
    Represents a customer with a name, address, and cart.

    Attributes
    ----------
    name : str
        The name of the customer.
    address : str
        The address of the customer.
    cart : dict
        Dictionary containing food items and their quantities in the cart.
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cart = {}

    def add_to_cart(self, food_item, quantity):
        """
        Adds a food item to the customer's cart.

        Parameters
        ----------
        food_item : FoodItem
            The food item to add to the cart.
        quantity : int
            The quantity of the food item to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if food_item in self.cart:
            self.cart[food_item] += quantity
        else:
            self.cart[food_item] = quantity

    def remove_from_cart(self, food_item, quantity):
        """
        Removes a food item from the customer's cart.

        Parameters
        ----------
        food_item : FoodItem
            The food item to remove from the cart.
        quantity : int
            The quantity of the food item to remove.
        """
        if food_item in self.cart:
            if self.cart[food_item] <= quantity:
                del self.cart[food_item]
            else:
                self.cart[food_item] -= quantity
        else:
            raise ValueError(f"{food_item.name} not found in the cart.")


class DeliveryService:
    """
    Represents a delivery service that manages restaurants.

    Attributes
    ----------
    restaurants : list
        List of restaurants managed by the delivery service.
    """
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        """
        Adds a restaurant to the delivery service.

        Parameters
        ----------
        restaurant : Restaurant
            The restaurant to add.
        """
        self.restaurants.append(restaurant)

    def find_restaurant_by_name(self, name):
        """
        Finds a restaurant by its name.

        Parameters
        ----------
        name : str
            The name of the restaurant to find.

        Returns
        -------
        Restaurant or None
            The restaurant if found, otherwise None.
        """
        for restaurant in self.restaurants:
            if restaurant.name == name:
                return restaurant
        return None


# Test the food delivery system
restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Spice Delight")

food_item1 = FoodItem("Burger", 8)
food_item2 = FoodItem("Pizza", 12)
food_item3 = FoodItem("Pasta", 10)

restaurant1.add_to_menu(food_item1, 10)
restaurant1.add_to_menu(food_item2, 5)

restaurant2.add_to_menu(food_item2, 8)
restaurant2.add_to_menu(food_item3, 12)

customer = Customer("Alice", "123 Main St.")
customer.add_to_cart(food_item1, 2)
customer.add_to_cart(food_item2, 3)

delivery_service = DeliveryService()
delivery_service.add_restaurant(restaurant1)
delivery_service.add_restaurant(restaurant2)

try:
    # This should raise a ValueError
    customer.add_to_cart(food_item3, -2)
except ValueError as e:
    print(e)

try:
    # This should raise a ValueError
    restaurant1.remove_from_menu(food_item2, 6)
except ValueError as e:
    print(e)

try:
    # This should raise a ValueError
    restaurant2.remove_from_menu(food_item1, 1)
except ValueError as e:
    print(e)

print("Total revenue for Tasty Bites:", restaurant1.get_total_revenue())
print("Total revenue for Spice Delight:", restaurant2.get_total_revenue())

