def modify_elements(items):
    """Multiplies all element values in items by 2."""
    # Cannot pass tuple to this function because tuploes not mutible
    for i in range(len(items)):
        items[i] *= 2

numbers = [10, 3, 7, 1, 9]
modify_elements(numbers)

print("numbers after modification: {}".format(numbers))