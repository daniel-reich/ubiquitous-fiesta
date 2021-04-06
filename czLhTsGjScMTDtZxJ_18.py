
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True
​
def primorial(n):
    if n == 1:
        return 2
    from functools import reduce
    lst = [x for x in range(n * n) if is_prime(x)][0:9]
    return reduce(lambda x, y: x * y, lst[0:n])

