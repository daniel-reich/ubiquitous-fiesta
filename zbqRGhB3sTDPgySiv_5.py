
from math import factorial
​
def mod(base, key):
    loop = 0
    key = factorial(key)
    # for i in range(base):
    #    loop += factorial(i) % key
    # return loop % key
    if base <= 0:
      return 0
​
    n = 1 % key
    for i in range(base - 1, 0, -1):
      n = (n * i + 1) % key
        
    return n

