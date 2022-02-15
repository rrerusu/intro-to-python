# exercise 02 - 05
"""Determine a circle's area, circumference, and diameter from a given radius"""

# The book said to use 3.14159 as PI
pi = 3.14159
radius = 2

# Values to calculate
diameter = radius * 2
circumference = diameter * pi
area = radius ** 2 * pi

# Output values
print("Circle with radius of 2 has diameter of {}, circumference of {}, and area of {}".format(
    diameter, circumference, area
))