
from math import factorial
​
def mod(base, key):
    k=(min(base,key))
    loop = 0
    key = factorial(key)
    for i in range(k):
        loop += factorial(i) % key
    return loop % key

