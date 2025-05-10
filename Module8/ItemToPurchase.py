class ItemToPurchase:

    # Constructor/Initializer method
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def __init__(self, item_name:str, item_price:float, item_quantity:int, item_description:str):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Instance method
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print("Iem cost:",cost)

    # Return the cost of item
    def get_total_cost(self):
        cost = self.item_price * self.item_quantity
        return cost

    def print_item_description(self):
        print(self.item_name,":",self.item_description)

    def item_report_record(self):
        print(self.item_name, " ", self.item_quantity, " @ $", self.item_price, " = $", self.get_total_cost(), sep="")
