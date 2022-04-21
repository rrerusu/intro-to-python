# Example 05 - 12: List Comprehension
'''Functional style features of python list creation'''

list1 = []
for item in range(1, 6):
    list1.append(item)

print("List1 using for loop: {}".format(list1))

list2 = [item for item in range(1, 6)]
print("List2 using list comprehension: {}".format(list2))

list3 = [item ** 3 for item in range(1, 6)]
print("List3: {}".format(list3))

list4 = [item for item in range(1, 11) if item % 2 == 0]
print("list4: {}".format(list4))

colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [item.upper() for item in colors]
print("colors2 = {}".format(colors2))
print("colors = {}".format(colors))