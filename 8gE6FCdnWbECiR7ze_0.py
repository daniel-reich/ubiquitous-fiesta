
import itertools
​
def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
​
def factors(n):
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
def digital_root(n):
    r = 0
    while n > 0:
        r += n % 10
        n //= 10
    return r if r < 10 else digital_root(r)
​
def is_smith(n):
    if n in primes:
        return True
    fac_sum = sum(list(factors(n)))
    return digital_root(n) == digital_root(fac_sum)
​
primes = set(primes2(10**5))
​
def smith_type(n):
    if n in primes:
        return "Trivial Smith"
    if is_smith(n):
        if is_smith(n + 1) and n + 1 not in primes:
            return "Youngest Smith"
        if is_smith(n - 1) and n - 1 not in primes:
            return "Oldest Smith"
        return "Single Smith"
    return "Not a Smith"

