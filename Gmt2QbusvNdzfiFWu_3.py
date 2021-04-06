
def gen_primes(n):
    primes = {2}
    for k in range(3, n, 2):
        if all(k % p > 0 for p in primes):
            primes.add(k)
    return sorted(primes)
​
lst_p = gen_primes(224)
​
def sum_prime(lst):
    res = ''
    for p in lst_p:
        if p > lst[-1]:
            break
        s = sum(n for n in lst if not n % p)
        if s > 0:
            res += '({} {})'.format(p, s)
    return res

