# exercise 02 - 08
"""Print a table of squares and cubes"""

print("Left justiied table:")
print("{:<8s}{:<8s}{:<8s}".format(
    "number", "square", "cube"
))

for i in range(6):
    print("{:<8d}{:<8d}{:<8d}".format(
        i, i ** 2, i ** 3
    ))

print("Right justiied table:")
print("{:>8s}{:>8s}{:>8s}".format(
    "number", "square", "cube"
))

for i in range(6):
    print("{:>8d}{:>8d}{:>8d}".format(
        i, i ** 2, i ** 3
    ))