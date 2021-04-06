
from math import factorial
​
def mod(base, key):
    loop = sum([factorial(i) if i < key else 0 for i in range(base)])
    return loop % factorial(key)

