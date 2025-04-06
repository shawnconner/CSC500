# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food and then calculate
# the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts
# and the total price.

#Contants
TIP_PCT = .18
TAX_PCT =  .07

# Given an amount calculate pct value
def calculatePct(amount, pct_amt):
    return amount * pct_amt # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    amount = int(input('Enter amount of Meal \n'))

    #calulate tax, tip, and total
    tip = calculatePct(amount,TIP_PCT)
    tax = calculatePct(amount,TAX_PCT)
    total = amount + tip + tax

    #Display the receipt
    print("Meal charge: $", amount)
    print("Tip:         $", round(tip,2))
    print("Tax:         $", round(tax,2))
    print("-------------")
    print("Total:       $", round(total,2))