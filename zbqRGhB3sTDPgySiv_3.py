
from math import factorial
​
def mod(base, key):
    loop = 0
    for i in range(min(base,key)):
        loop += factorial(i)
    return key>1 and loop

