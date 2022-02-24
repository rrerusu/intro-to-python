# exercise 03 - 15
'''Approximate e'''

def calc_factorial(number):
    '''Calculate the factorial of a number'''
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial

def approx_e():
    e = 0
    for i in range(0, 101):
        e += 1 / calc_factorial(i)
        print("{}\t{}".format(
            i + 1,
            e
        ))

approx_e()