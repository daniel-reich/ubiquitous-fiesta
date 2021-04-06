
def gen_primes(n):
    primes = {2}
    for k in range(3, n, 2):
        if all(k % p > 0 for p in primes):
            primes.add(k)
    return sorted(primes)
​
lst_p = gen_primes(3444)
set_p = set(lst_p)
​
def goldbach_conjecture(n):
    if n > 2 and not n % 2:
        for p in lst_p:
            if n - p in set_p:
                return [p, n - p]
    return []

