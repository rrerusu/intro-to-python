# exercise 03 - 16
'''Determine the two largest of 10 numbers'''

def determine_two_largest():
    largest = None
    second_largest = None
    for i in range(10):
        num = int(input("Enter num {}: ".format(i + 1)))

        if largest == None:
            largest = num
        elif second_largest == None:
            if largest > num:
                second_largest = num
            else:
                second_largest = largest
                largest = num
        elif largest < num:
            second_largest = largest
            largest = num
        elif second_largest < num:
            second_largest = num
    
    print("Largest: {}\nSecond largest: {}".format(
        largest, second_largest
    ))

determine_two_largest()