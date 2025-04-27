from Module6.ItemToPurchase import ItemToPurchase
from Module6.ShoppingCart import ShoppingCart

def display_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def print_menu(cart:ShoppingCart):
    selection = "a"
    display_menu()

    while selection != "q":
        selection = input("Choose an option: ")

        if selection == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif selection == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif selection == "a":
            print("ADD ITEM TO CART")
            current_name = input("Enter the item name: ")
            current_price = float(input("Enter the item price: "))
            current_quantity = int(input("Enter the item quantity: "))
            current_description = input("Enter the item description: ")
            cart.add_item(ItemToPurchase(current_name, current_price, current_quantity, current_description))
        elif selection == "r":
            print("REMOVE ITEM FROM CART")
            current_name = input("Enter name of item to remove: ")
            cart.remove_item(current_name)
        elif selection == "c":
            print("CHANGE ITEM QUANTITY")
            current_name = input("Enter the item name: ")
            current_quantity = int(input("Enter the new quantity: "))
            # Find current values for item so that only the quantity gets updated.
            current_item = cart.find_item(current_name)
            cart.modify_item(ItemToPurchase(current_name, current_item.item_price, current_quantity, current_item.item_description))
        elif selection == "q":
            print("Quitting shopping cart")
        else:
            print("Invalid selection, please try again.")

if __name__ == '__main__':
    cart = ShoppingCart("Shawn Conner", "April 26, 2025")
    print_menu(cart)

