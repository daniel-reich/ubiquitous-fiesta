
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
primes = primes2(10**5)
​
def get_closest_prime(k):
    if k < 3:
        return 2 - k, 2
    idx = bisect.bisect_left(primes, k)
    if primes[idx] == k:
        # k is prime itself but, so consider prev and next prime:
        if primes[idx + 1] - k <= k - primes[idx - 1]:
            return primes[idx + 1] - k, primes[idx + 1]
        else:
            return k - primes[idx - 1], primes[idx - 1]       
    if primes[idx] - k <= k - primes[idx - 1]:
        return primes[idx] - k, primes[idx]
    else:
        return k - primes[idx - 1], primes[idx - 1]
​
def loneliest_number(lo, hi):
    if hi <= 2:
        return {'number': lo, 'distance': lo, 'closest': 2}
    rec_dist, closest = get_closest_prime(lo)
    number = lo
    for k in range(lo + 1, hi + 1):
        dist, p = get_closest_prime(k)
        if dist > rec_dist:
            rec_dist = dist
            closest = p
            number = k
    return {'number': number, 'distance': rec_dist, 'closest': closest}

