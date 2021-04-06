
def is_powerful(n):
    factors = [i for i in range(2,n+1) if n % i == 0]
    i = 2
    p_factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            p_factors.append(i)
    if n > 1:
        p_factors.append(n)
    p_factors = [x**2 for x in set(p_factors)]
 
    return set(p_factors).issubset(set(factors))

