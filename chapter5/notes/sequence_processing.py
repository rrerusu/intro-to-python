# example 5 - 15
'''Extra sequence processing functions'''
print("'Red' < 'orange': {}".format('Red' < 'orange'))
print("ord('R'): {}".format(ord('R')))
print("ord('o'): {}".format(ord('o')))
print("\n")

colors = ['Red', 'orange', 'Yellow', "green", "Blue"]
print("colors: {}".format(colors))
print("Minimum value in colors: {}".format(
    min(colors, key = lambda s: s.lower())
))
print("Maximum value in colors: {}".format(
    max(colors, key = lambda s: s.lower())
))
print("\n")

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
reversed_numbers = [item ** 2 for item in reversed(numbers)]
print("Numbers reversed and squared: {}".format(reversed_numbers))
print("\n")

names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0, 3.75]
for name, gpa in zip(names, grade_point_averages):
    print(f'Name = {name}; GPA = {gpa}')
print("\n")

foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']
print("Minimum value in foods w/o case change: {}".format(
    min(foods)
))
print("Minimum value in foods w/ case change: {}".format(
    min(foods, key = lambda f: f.lower())
))
print("\n")

nums1 = [10, 20, 30]
nums2 = [10, 20, 30]
nums_sum = []
for num1, num2 in zip(nums1, nums2):
    nums_sum.append(num1 + num2)
print("Sum of numbers in 2 lists: {}".format(nums_sum))