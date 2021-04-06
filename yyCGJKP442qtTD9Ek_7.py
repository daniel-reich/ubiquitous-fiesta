
def sums_of_powers_of_two(n):
    lst = []
    while n > 0:
        x = 0
        while 2**x <= n:
            x += 1
        lst += [2**(x - 1)]
        n -= 2**(x - 1)
    return lst[::-1]

