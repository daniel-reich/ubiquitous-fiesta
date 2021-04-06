
def prime_factors(n):
    factors = [1]
    while n > 1:
        for d in range(2, n+1):
            if n % d == 0:
                factors.append(d)
                n = int(n/d)
​
    return factors
​
def lcm_three(num):
    factors = {}
​
    for n in num:
        factor = prime_factors(n)
        for f in factor:
            if f not in factors.keys():
                factors[f] = factor.count(f)
            else:
                if factor.count(f) > factors[f]:
                    factors[f] = factor.count(f)
    lcm = 1
    for p in factors.keys():
        for _ in range(factors[p]):
            lcm *= p
    return lcm

