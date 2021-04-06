
from random import randint
def is_prime(n, k=5): 
    if n < 2:
        return False
    s = 0
    d = n-1
    while d % 2 == 0:
        s = s+1
        d = d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: 
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: 
            return False
    return True

