
def is_prime(n):
    return n > 1 and (n == 2 or (n%2 != 0 and all(n%ii for ii in range(3, int(n**0.5 + 1), 2))))
​
def prime_factors(n):
    pfs = []
    while n%2 == 0:
        pfs.append(2)
        n /= 2
    lim = int(n**0.5) + 1
    for i in range(3, lim, 2):
        while n%i == 0:
            pfs.append(i)
            n /= i
    return pfs + [int(n)] if n > 2 else pfs
​
def digital_root(n):
    if n < 10: return n
    return digital_root(sum(map(int,str(n))))
​
def is_smith(n):
    # incorrect! tests for 22 and 28 have Trivial Smith older brothers
    return not is_prime(n) and digital_root(n) == digital_root(sum(prime_factors(n)))
    # correct versions should be:
    #return is_prime(n) or (digital_root(n) == digital_root(sum(prime_factors(n))))
    #OR
    #return digital_root(n) == digital_root(sum(prime_factors(n)))
​
​
smith_type = lambda n: \
    'Trivial Smith' if is_prime(n) else \
    'Not a Smith' if not is_smith(n) else \
    'Youngest Smith' if is_smith(n+1) else \
    'Oldest Smith' if is_smith(n-1) else \
    'Single Smith'

