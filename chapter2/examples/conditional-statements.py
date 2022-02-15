"""Comparing integers if using statements and comparison operators."""

print('Enter two integers, and I will tell you',
    'the relationships they satisfy.')

number1 = int(input('Enter the first integer: '))
number2 = int(input('Enter the second integer: '))

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)