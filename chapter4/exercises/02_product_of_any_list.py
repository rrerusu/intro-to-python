# exercise 04 - 13
'''Calculate the product of all numbers in any list'''

def calcProduct(nums):
    '''Calculate product of values in a list'''
    product = 1
    for i in nums:
        product *= i
    return product

myNums = []

list_len = int(input("Enter length of the list: "))

# Get values for array
for i in range(list_len):
    myNums += [int(input(f"Enter number {i + 1}: "))]

print(f"Sum of numbers is: {calcProduct(myNums)}")