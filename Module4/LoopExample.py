total = 0
current_amount = 1

while current_amount != 0:
    current_amount = int(input('Enter amount of Meal(enter 0 to end): '))
    total+=current_amount

print('Total:', total)