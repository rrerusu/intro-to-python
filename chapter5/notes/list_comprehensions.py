# Example 05 - 12: List Comprehension
'''Functional style features of python list creation'''

list1 = []
for item in range(1, 6):
    list1.append(item)

print("List1 using for loop: {}".format(list1))

list2 = [item for item in range(1, 6)]
print("List2 using list comprehension: {}".format(list2))