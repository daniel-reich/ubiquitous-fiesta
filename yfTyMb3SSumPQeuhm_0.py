
from math import log2
​
def fibonacci(n):
    n = int(log2(n))
    a, b = 1, 1
    for _ in range(n-1):
        b2 = b*b
        a, b = a*a + b2, 2*a*b + b2
    return b

