numbers = [3, 7, 1, 4, 2, 8, 5, 6]
print("numbers.index(5): {}\n".format(numbers.index(5)))

numbers *= 2
print("numbers *= 2: {}\n".format(numbers))

print("numbers.index(5, 7): {}".format(numbers.index(5, 7)))

print("numbers.index(7, 0, 4): {}\n".format(numbers.index(7, 0, 4)))

print("1000 in numbers: {}".format(1000 in numbers))

print("5 in numbers: {}\n".format(5 in numbers))

print("1000 not in numbers: {}".format(1000 not in numbers))

print("5 not in numbers: {}".format(5 not in numbers))

key = 1000
if key in numbers:
    print(f'found {key} at index {numbers.index(key)}')
else:
    print(f'{key} not found')