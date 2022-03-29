color_names = ['orange', 'yellow', 'green']
color_names.insert(0, 'red')
print("color_names.insert(0, 'red'): {}".format(color_names))

color_names.append('blue')
print("color_names.append('blue'): {}".format(color_names))

color_names.extend(['indigo', 'violet'])
print("color_names.extend(['indigo', 'violet']): {}".format(color_names))

sample_list = []
s = 'abc'
sample_list.extend(s)
print("sample_list.extend(s): {}".format(sample_list))

t = (1, 2, 3)
sample_list.extend(t)
print("sample_list.extend(t): {}".format(sample_list))

sample_list.extend((4, 5, 6))
print("sample_list.extend((4, 5, 6)): {}\n".format(sample_list))

color_names.remove("green")
print("color_names.remove('green'): {}".format(color_names))

color_names.clear()
print("color_names.clear(): {}\n".format(color_names))


responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')
print("\n")

copied_list = color_names.copy()
print("copied_list: {}".format(copied_list))