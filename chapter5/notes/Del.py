numbers = list(range(10))

del numbers[-1]
print("Del numbers[-1]: ", end="")
print(numbers)

del numbers[0:2]
print("Del numbers[0:2]: ", end="")
print(numbers)

del numbers[::2]
print("Del numbers[::2]: ", end="")
print(numbers)

del numbers[:]
print("Del numbers[:]: ", end="")
print(numbers)
