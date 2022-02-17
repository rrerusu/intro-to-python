# exercise 03 - 08
"""Split the digits of a number"""

number = int(input("Enter number: "))

# Calculate length of number
length_number = 1
while number // (10 ** length_number) > 0:
    length_number += 1

# split each digit apart
for digit in range(length_number):
    print("{}    ".format(number // (10 ** (length_number - digit - 1))), end="")
    number = number % (10 ** (length_number - digit - 1))