
from math import sqrt
def mystery_func(num):
    a='2'*int(sqrt(num))
    b=str(num-2**int(sqrt(num)))
    return int(a+b)

