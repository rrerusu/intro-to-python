# Example 05 - 14: Filter, Map, and Reduce
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
def is_odd(x):
    '''Return True if x is odd.'''
    return x % 2 != 0

print("Filtering odd numbers: {}".format(list(filter(is_odd, numbers))))
print("Filtering odd numbers: {}".format([item for item in numbers if is_odd(item)]))
print("Filtering odd numbers: {}".format(
    list(filter(lambda x: x % 2 != 0, numbers))
))

print("Squaring numbers: {}".format(list(map(lambda x: x ** 2, numbers))))
print("Squaring numbers: {}".format([item ** 2 for item in numbers]))

print("Square of odd numbers: {}".format(
    list(map(lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, numbers)))
))
print("Square of odd numbers: {}".format([x ** 2 for x in numbers if x % 2 != 0]))

numbers = list(range(1, 16))
print("\nList of even numbers: {}".format(list(filter(
    lambda x: x % 2 == 0, numbers
))))

print("List of squared numbers: {}".format(list(map(
    lambda x: x ** 2, numbers
))))
print("List of squared even numbers: {}".format(list(
    map(lambda x: x ** 2, filter(
        lambda x: x % 2 == 0, numbers
    ))
)))

print("\n")
fahrenheit_temps = [41, 32, 212]
print("List of fahrenheit and celsius counterpart temperatures: {}".format(
    list(map(
        lambda x: (x, (x - 32) * 5 / 9), fahrenheit_temps
    ))
))