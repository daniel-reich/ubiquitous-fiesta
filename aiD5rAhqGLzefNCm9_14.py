
from random import randint
​
# Using Miller-Rabin primality test
def is_prime(n):
    k, t, d = 10, 0, n - 1
​
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
​
    while d%2 == 0:
        t += 1
        d //= 2
    for _ in range(k):
        a = randint(2, n - 1)
        res = pow(a, d, n)
        if res == 1:
            continue
        for _ in range(t - 1):
            if res == n - 1:
                break
            res = pow(res, 2, n)
        if res != n - 1:
            return False
    return True

