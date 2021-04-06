
from math import factorial
​
def mod(base, key):
    loop = 1 if key > 1 else 0
    factor, key = key, factorial(key)
    for i in range(min(base, factor)-1, 0, -1):
        loop = (loop*i + 1) % key
    return loop

