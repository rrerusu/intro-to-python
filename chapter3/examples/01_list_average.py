# example 03 - 01
"""Class average program with sequence-controlled repitition."""

total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade
    grade_counter += 1

average = total / grade_counter
print(f'Class average is {average}')