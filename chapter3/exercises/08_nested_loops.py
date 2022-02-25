# exercise 03 - 18
'''display asterisk triangles'''

def display_triangles():
    '''display triangles made of asterisks'''
    print("{:10s}\t{:10s}\t{:10s}\t{:10s}".format("(a)", "(b)", "(c)", "(d)"))

    # display triangles
    triangle1 = triangle2 = triangle3 = triangle4 = ""
    for counter in range(1, 11):
        triangle1 = triangle4 = "*" * counter
        triangle2 = triangle3 = "*" * (11 - counter)
        print("{:<10}\t{:<10s}\t{:>10s}\t{:>10s}".format(
            triangle1, triangle2, triangle3, triangle4
        ))

display_triangles()