
def smallest(digits, value):
    d = 10 ** (digits - 1)
    while d % value != 0:
        d += 1
    return d

