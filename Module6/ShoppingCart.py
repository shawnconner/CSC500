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


    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.get_total_cost()
        return total_cost

    #Outputs total of objects in cart.
    #If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name, "'s Shopping Cart - ", self.current_date, sep="" )
            print("Number of Items:", self.get_num_items_in_cart())
            for item in self.cart_items:
                item.item_report_record()
            print("Total: $", self.get_cost_of_cart(), sep="")

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name, "'s Shopping Cart - ", self.current_date, sep="")
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()
