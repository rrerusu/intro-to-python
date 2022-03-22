from turtle import color


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

numbers.sort()
print("numbers.sort(): {}".format(numbers))

numbers.sort(reverse=True)
print("numbers.sort(reverse=True: {})".format(numbers))

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
asending_numbers = sorted(numbers)
print("ascending_numbers: {}".format(asending_numbers))
print("numbers: {}".format(numbers))

letters = 'fadgchjebi'
ascending_letters = sorted(letters)
print("ascending_letters: {}".format(ascending_letters))
print("letters: {}".format(letters))

colors = ('red', 'orange', 'yellow', 'green', 'blue')
ascending_colors = sorted(colors)
print("ascending_colors: {}".format(ascending_colors))
print("colors: {}".format(colors))