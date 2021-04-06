
def rearranged_difference(num):
    digits = sorted([d for d in str(num)])
    return int(''.join(digits[::-1])) - int(''.join(digits))

