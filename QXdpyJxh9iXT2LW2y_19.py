
import bisect
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
limit = 10**4
primes = primes2(limit)
​
semis, square_free = set(), set()
for p1 in primes:
    for p2 in primes:
        p = p1 * p2
        if p > limit:
            break
        semis.add(p)
        if p1 != p2:
            square_free.add(p)
semis = sorted(list(semis))
square_free = sorted(list(square_free))
​
def semiprimes(n):
    idx1 = bisect.bisect_right(semis, n)
    idx2 = bisect.bisect_right(square_free, n)
    A = semis[:idx1]
    B = square_free[:idx2]
    return (A, B)

