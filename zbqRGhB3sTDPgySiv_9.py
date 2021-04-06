
from math import factorial
​
def mod(base, key):
    loop = 0
    key2 = factorial(key)
    for i in range(min(base, key)):
        loop += factorial(i) % key2
    return loop % key2

