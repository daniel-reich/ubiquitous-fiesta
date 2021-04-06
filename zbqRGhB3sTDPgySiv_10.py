
from math import factorial
def mod(base, key):
    loop = 0
    key = factorial(key)
    for i in range(base):
        loop += factorial(i) % key
        if factorial(i) % key == 0:
            break
    return loop

