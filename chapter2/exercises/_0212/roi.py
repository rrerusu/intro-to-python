# exercise 02 - 11
"""Calculate return on investment"""

r = 0.07
p = 1000
years = range(10, 31, 10)

for n in years:
    print("Investment after {} years = {}".format(
        n, p * (1 + r) ** n
    ))