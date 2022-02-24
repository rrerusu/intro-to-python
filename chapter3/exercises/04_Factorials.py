def calcFactorial(number):
    '''Calculate the factorial of a number'''
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

print(calcFactorial(10))
print(calcFactorial(20))
print(calcFactorial(30))