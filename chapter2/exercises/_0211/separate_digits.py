# exercise 02 - 11
"""Seperate digits of input number"""
number = input("Enter number: ")

for i in range(len(number)):
    print("{}{}".format(number[i], "    " if i < len(number) - 1 else ""), end="")