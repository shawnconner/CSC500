from Module6.ItemToPurchase import ItemToPurchase
from Module6.ShoppingCart import ShoppingCart

if __name__ == '__main__':

    # Loop to get 2 items
    print("Enter 2 items\n")
    cart= ShoppingCart("Shawn Conner", "April 26, 2025")
    for i in range(2):
        print("Item", i+1)

        current_name = input("Enter the item name: ")
        current_price = float(input("Enter the item price: "))
        current_quantity = int(input("Enter the item quantity: "))

        cart.add_item(ItemToPurchase(current_name, current_price, current_quantity,current_name))
        print()

    print("get_num_items_in_cart: ", cart.get_num_items_in_cart())
    print("get_cost_of_cart: ", cart.get_cost_of_cart())
    cart.print_total()
    cart.print_descriptions()
