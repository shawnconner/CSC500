from Module4.ItemToPurchaseOld import ItemToPurchaseOld


if __name__ == '__main__':

    # Loop to get 2 items
    print("Enter 2 items\n")
    items = []
    for i in range(2):
        print("Item", i+1)

        current_name = input("Enter the item name: ")
        current_price = float(input("Enter the item price: "))
        current_quantity = int(input("Enter the item quantity: "))

        items.append(ItemToPurchaseOld(current_name, current_price, current_quantity))
        print()

    # Loop thorugh items and print out the cost of each itme and then the total
    print("TOTAL COST")

    total = 0
    for item in items:
        cost = item.item_price*item.item_quantity
        total+=cost

        print(item.item_name, " ",  item.item_quantity, " @ $", item.item_price, " = $", cost, sep="")

    print("Total: $", total, sep="")
