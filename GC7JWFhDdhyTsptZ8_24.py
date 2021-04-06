
def sexy_primes(n, limit):
    '''
    Returns a sorted list of n-length tuples of sexy primes as described in the
    instructions.
    '''
    from itertools import combinations
    
    is_prime = lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
​
    primes = [i for i in range(2, limit) if is_prime(i)]
    
    return [combo for combo in combinations(primes, n) \
            if all(b == a + 6 for a,b in zip(combo, combo[1:]))]

