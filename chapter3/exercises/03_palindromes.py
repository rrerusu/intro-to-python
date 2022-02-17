# exercise 03 - 12
"""Determines whether a number is a palindrome or not"""

number = int(input("Enter number: "))

# Calculate length of number
length_number = 1
while number // (10 ** length_number) > 0:
    length_number += 1

# split each digit apart
number_reversed = 0
original_number = number
for digit in range(length_number):
    number_reversed += (number // (10 ** (length_number - digit - 1))) * 10 ** digit
    number = number % (10 ** (length_number - digit - 1))

print("{} is{} a palindrome.".format(original_number, ("" if original_number == number_reversed else "n't")))