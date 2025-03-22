#multiply 2 numbers
def multiply(number1, number2):
    return number1 * number2  # Press ⌘F8 to toggle the breakpoint.

#divide 2 numbers
def divide(number1, number2):
    return number1 / number2


if __name__ == '__main__':
    num1 = int(input('Enter number 1\n'))
    num2 = int(input('Enter number 1\n'))

    print('Number 1:', num1, ' + Number 2:', num2, ":", multiply(num1, num2))
    print('Number 1:', num1, ' - Number 2:', num2, ":", divide(num1, num2))
