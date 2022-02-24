# exercise 03 - 14
'''Approximate the digits of pi'''

def approximatePi():
    pi = 0 
    for i in range(1, 1000):
        pi += ((-1) ** (i + 1)) * 4 / (2 * i - 1)
        print("{}\t{}".format(
            i,
            pi)
        )

approximatePi()