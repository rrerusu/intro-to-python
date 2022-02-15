# exercise 02 - 15
"""Sort 3 floats in ascending order"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)
middle = 0
if smallest < num1 < largest:
    middle = num1
elif smallest < num2 < largest:
    middle = num2
else:
    middle = num3

print("Numbers in ascending order are: {}, {}, and {}".format(smallest, middle, largest), end="")