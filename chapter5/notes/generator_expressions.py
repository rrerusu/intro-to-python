# Example 05 - 13: Generator expressions
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
print("\nsquares_of_odds: {}".format(squares_of_odds))