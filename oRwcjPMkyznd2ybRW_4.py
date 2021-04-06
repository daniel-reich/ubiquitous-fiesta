
from functools import reduce
def max_product(n):
    max = 1
    for i in range(n+1):
        if prods(i) > max:
            max = prods(i)
    return [i for i in range(n+1) if prods(i) == max]
​
def prods(n):
    return int(reduce(lambda x,y: int(x)*int(y), str(n)))

