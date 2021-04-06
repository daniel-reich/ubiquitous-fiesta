
import math
import itertools
from collections import Counter
​
def get_factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n
​
def squares_sum(n):
    root = int(round(math.sqrt(n), 0))
    if n <= 2:
        return True
    if root**2 == n:
        # n is a perfect square, so it can be written as (sqrt(n))^2 + 0^2
        return True
    # n is a sum of squares iff each prime factor is of form 4k+1
    C = Counter(list(get_factors(n)))
    for f, c in C.items():
        if f != 2 and c % 2 == 1 and (f - 1) % 4 != 0:
            return False
    return True

