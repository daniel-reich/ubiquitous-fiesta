
import math
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
​
def non_repeats(radix):
    return math.floor(math.exp(1)*(radix-1)*fact(radix-1))

