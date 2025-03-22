
# Add 2 number s
def add(number1, number2):
    return number1 + number2 # Press ⌘F8 to toggle the breakpoint.

# Subtract 2 numbers
def subtract(number1, number2):
    return number1 - number2

if __name__ == '__main__':
    num1 = int(input('Enter number 1\n'))
    num2 = int(input('Enter number 1\n'))

    print('Number 1:', num1,' + Number 2:',num2,":", add(num1,num2))
    print('Number 1:', num1,' - Number 2:',num2,":", subtract(num1,num2))

