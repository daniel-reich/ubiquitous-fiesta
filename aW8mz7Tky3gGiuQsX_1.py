
from math import sqrt
def is_powerful(n):
    while (n % 2 == 0):
        p = 0
        while (n % 2 == 0):
            n //= 2
            p += 1
        if (p == 1):
            return False
    for f in range(3, int(sqrt(n)) + 1, 2):
        p = 0
        while (n % f == 0):
            n //= f
            p = p + 1
        if (p == 1):
            return False
    return (n == 1)

