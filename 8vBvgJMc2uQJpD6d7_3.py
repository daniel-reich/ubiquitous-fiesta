
def prime_factors(n):
    a = []
    f = 2
    while n > 1:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 1
    return a

