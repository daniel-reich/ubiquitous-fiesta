
def prime_factorization(n):
    res = []
    for i in range(2, int(n**0.5) + 1): 
        while not n%i: 
            res.append(i) 
            n //= i
    return res + [n] if n > 1 else res
​
def sum_prime(lst):
    groups = [(i, set(prime_factorization(i))) for i in lst]
    res = {}
    for n, factors in groups:
        for f in factors:
            if f in res:
                res[f] += n
            else:
                res[f] = n
    return ''.join('({} {})'.format(k, v) for k, v in sorted(res.items()))

