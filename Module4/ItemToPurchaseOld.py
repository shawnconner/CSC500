class ItemToPurchaseOld:

    # Constructor/Initializer method
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def __init__(self, item_name:str, item_price:float, item_quantity:int):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Instance method
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print("Iem cost:",cost)

