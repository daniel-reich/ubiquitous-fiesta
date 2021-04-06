
from itertools import compress
from bisect import bisect_left as bl
​
def rwh_primes1v2(n):
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2]+list(compress(range(3,n,2), sieve[1:]))
​
def loneliest_number(lo, hi):
    lst = rwh_primes1v2(int(1.05*hi))
    interval = bl(lst, lo)
    lst = lst[interval - 1 if interval >= 1 else interval:bl(lst, hi)+1]
    first = abs(lst[0] - lo)
    maxi = [lo, first, lst[0]]
    for i in range(1, len(lst)):
        new = lst[i] - lst[i-1]
        comp = min([new, 0], [first, 1])
        first = new
        if comp[0] > maxi[1]:
            maxi = [lst[i-1], comp[0], lst[i-2*comp[1]]]
        if new//2 > maxi[1]:
            maxi = [(lst[i] + lst[i-1])//2, new//2, lst[i]]
    return {'number': maxi[0], 'distance': maxi[1], 'closest': maxi[2]}

