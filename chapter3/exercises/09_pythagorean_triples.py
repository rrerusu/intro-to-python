# exercise 03 - 19
'''display all pythagorean triples smaller than 20'''

def print_pythagorean_triples():
    '''display all pythagorean triples below 20'''
    for leg1 in range(1, 21):
        for leg2 in range(leg1, 21):
            hypotenuse = calc_hypotenuse(leg1, leg2)
            if hypotenuse % 1 == 0 and hypotenuse < 20:
                print("{}, {}, {}".format(
                    leg1, leg2, int(hypotenuse)
                ))

def calc_hypotenuse(leg1, leg2):
    '''calculate hypotenuse from leg1 and leg2'''
    return (leg1 ** 2 + leg2 ** 2) ** 0.5

print_pythagorean_triples()