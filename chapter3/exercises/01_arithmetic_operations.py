# exercise 03 - 08
"""Arithmetic operations on 4 numbers"""
numbers = []
for i in range(4):
    numbers += [int(input("Enter number {}: ".format(i + 1)))]

sumation = 0
for i in numbers:
    sumation += i
print("Sum = {}".format(sumation))
print("Average = {}".format(sumation / len(numbers)))

product = 1
for i in numbers:
    product *= i
print("Product = {}".format(product))
print("Minimum = {}".format(min(numbers)))
print("Maximum = {}".format(max(numbers)))