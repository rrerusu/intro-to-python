# exercise 02 - 10
"""Calculate sum, average, product, largest, and smallest of 3 input nums"""

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))

# Print values after processing
print("Sum of {}, {}, and {} is {}".format(
    num1, num2, num3,
    num1 + num2 + num3
))
print("Average of {}, {}, and {} is {}".format(
    num1, num2, num3,
    (num1 + num2 + num3) / 3
))
print("Product of {}, {}, and {} is {}".format(
    num1, num2, num3,
    num1 * num2 * num3
))
print("Largest of {}, {}, and {} is {}".format(
    num1, num2, num3,
    max(num1, num2, num3)
))
print("Smallest of {}, {}, and {} is {}".format(
    num1, num2, num3,
    min(num1, num2, num3)
))