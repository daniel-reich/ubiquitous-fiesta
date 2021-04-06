
from math import factorial
​
def mod(base, key):
    if base == 1 and key == 1: return 0
    loop = 0
    if base > key:
        base, key = key, base
    for i in range(base):
        loop += factorial(i)
    return loop

