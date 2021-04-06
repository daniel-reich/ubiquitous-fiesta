
def is_prime(p):
    return all(p%ii!=0 for ii in range(2,p//2+1))
def sexy_primes(n, limit):
    if n <= 1:
        return [(p,) for p in range(2, limit) if is_prime(p)]
    return [tuple+(tuple[-1]+6,) for tuple in sexy_primes(n-1, limit-6) if is_prime(tuple[-1]+6)]

