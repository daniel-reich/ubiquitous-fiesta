
from itertools import count, islice
from functools import reduce
​
def primorial(n):
    primes = (n for n in count(2) if all(n%d for d in range(2, n)))
    return reduce(lambda a,b: a*b, islice(primes, 0, n))

