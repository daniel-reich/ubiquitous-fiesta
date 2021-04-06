
from math import sqrt
​
def is_prime(n: int) -> bool:
    if 2 <= n <= 3:
        return True
    if n%2==0:
        return False
    for i in range(3, n//2, 2):
        if n%i==0:
            return False
​
    return True
​
def next_prime(start: int) -> int:
    start += 1
    while not is_prime(start):
        start += 1
    return start
​
def double_p(n: int):
    factor = 2
    if is_prime(n):
        return False
    while factor <= n//2:
        if n%factor==0:
            quotient = int(n/factor)
            return (factor, quotient) if is_prime(quotient) else False
        factor = next_prime(factor)
​
def semiprimes(n):
    semi = []
    for i in range(4, n):
        if double_p(i):
            semi.append(i)
    no_square = list(filter(lambda x: not sqrt(x).is_integer(), semi))
    return semi, no_square

