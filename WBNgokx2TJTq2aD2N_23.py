
def smallest(digits, value):
    a = 10**(digits -1)
    for n in range(a, 5*a):
        if n % value == 0:
            return n

