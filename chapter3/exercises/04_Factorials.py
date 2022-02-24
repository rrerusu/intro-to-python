# exercise 3.13
'''Determine factorial of 10, 20, and 30'''

def calc_factorial(number):
    '''Calculate the factorial of a number'''
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

print(calc_factorial(10))
print(calc_factorial(20))
print(calc_factorial(30))