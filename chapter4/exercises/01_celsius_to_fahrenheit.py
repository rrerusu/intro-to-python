# exercise 04 - 09
'''Display from 0*C to 100*C in fahrenheit'''

def c_to_f(c):
    """Convert from celcius to fahrenheit"""
    return (9 / 5) * c + 32

print("{:<14}{:<7}".format(
    "Fahrenheit",
    "Celsius"
))

for temp in range(101):
    print("{:<14}{:<7}".format(
        temp, c_to_f(temp)
    ))