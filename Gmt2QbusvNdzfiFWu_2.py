
is_prime = lambda n: n > 1 and (n == 2 or (n%2 != 0 and all(n%ii for ii in range(3, int(n**0.5 + 1), 2))));
​
def sum_prime(lst):
    res = [(p, sum(v for v in lst if v % p == 0)) for p in range(2,  max(lst) + 1) if is_prime(p)]
    return ''.join(str(v) for v in res if v[1] > 0).replace(',', '')

