
def simplify_sqrt(n, a=1, i=3, ii = 9):
    while n % 4 == 0: a *= 2; n //= 4
    while ii <= n:
        while n % ii == 0: a *= i; n //= ii
        i += 2; ii = i**2
    return a, n

