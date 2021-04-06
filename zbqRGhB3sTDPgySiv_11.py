
import time
from math import factorial
​
facs = {k: factorial(k) for k in range(51)}
​
def mod(base, key):
    loop = 0
    key2 = key
    key = facs[key]
    for i in range(min(base, key2)):
        loop += facs[i] % key
    return loop % key

