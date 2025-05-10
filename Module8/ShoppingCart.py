from Module6.ItemToPurchase import ItemToPurchase

class ShoppingCart:

    # Constructor/Initializer method
    # customer_name(string) - Initialized in default constructor to "none"
    # current_date(string) - Initialized in default constructor to "January 1, 2020"
    # cart_items(list)
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

    # Parameterized constructor, which takes the customer name and date as parameters
    def __init__(self, customer_name:str, current_date:str):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item:ItemToPurchase):
        self.cart_items.append(item)

    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name:str):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                del self.cart_items[i]
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing removed.")

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    # If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
    # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item:ItemToPurchase):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                item_found = True
                if item.item_description  != "none" and item.item_quantity  != 0 and item.item_price != 0.0:
                    self.cart_items[i].item_description = item.item_description
                    self.cart_items[i].item_price = item.item_price
                    self.cart_items[i].item_quantity = item.item_quantity
                break

        if not item_found:
            print("Item not found in cart. Nothing modified.")


    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.get_total_cost()
        return total_cost

    # Outputs total of objects in cart.
    # If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name, "'s Shopping Cart - ", self.current_date, sep="" )
            print("Number of Items:", self.get_num_items_in_cart())
            for item in self.cart_items:
                item.item_report_record()
            print("Total: $", self.get_cost_of_cart(), sep="")

    # Outputs each item's description.
    # Added description to ItemToPurchase class
    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name, "'s Shopping Cart - ", self.current_date, sep="")
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()

    def find_item(self, item_name):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                return self.cart_items[i]
            else:
                return ItemToPurchase()