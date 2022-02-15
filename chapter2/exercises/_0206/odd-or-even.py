# exercise 02 - 06
"""Determine if a number is odd or even"""

number = int(input("Enter a number: "))

print("{} is {}.".format(
    number,
    "even" if number % 2 == 0 else "odd"
))