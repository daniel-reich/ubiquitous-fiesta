
def prime_factors(n): 
    factors = [] 
    while n%2 == 0: 
        factors.append(2) 
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2): 
        while n%i == 0: 
            factors.append(i) 
            n //= i
    return factors + [n] if n > 1 else factors
​
def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n
​
def is_smith(n):
    factors = prime_factors(n)
    if len(factors) == 1:
        return False
    return digital_root(n) == digital_root(sum(factors))
    
def smith_type(n):
    if n == 1:
        return 'Not a Smith'
    if len(prime_factors(n)) == 1:
        return 'Trivial Smith'
    young, middle, old = (is_smith(n-1), is_smith(n), is_smith(n+1))
    if not middle:
        return 'Not a Smith'
    d = {(True, True, False): 'Oldest Smith', 
         (False, True, True): 'Youngest Smith', 
         (False, True, False): 'Single Smith'}
    return d[young, middle, old]

