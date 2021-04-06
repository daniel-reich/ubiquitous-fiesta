
def binary_to_decimal(lst):
    sum = 0
    power = 7
    for each in lst:
        if each == 1:
            sum += 2**power
            power -= 1
        else:
            power -= 1
            continue
    return sum

