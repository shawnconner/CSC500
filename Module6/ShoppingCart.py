from Module6.ItemToPurchase import ItemToPurchase

class ShoppingCart:

    # Constructor/Initializer method
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

    def __init__(self, customer_name:str, current_date:str):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Instance method
    def add_item(self, item:ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name:str):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                del self.cart_items[i]
                item_found = True
                break

        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item:ItemToPurchase):


    def get_num_items_in_cart(self):
        cost = self.item_price * self.item_quantity
        print("Iem cost:",cost)

    def get_cost_of_cart(self):
        cost = self.item_price * self.item_quantity
        print("Iem cost:",cost)

    def print_total(self):
        cost = self.item_price * self.item_quantity
        print("Iem cost:",cost)

    def print_descriptions(self):
        cost = self.item_price * self.item_quantity
        print("Iem cost:",cost)