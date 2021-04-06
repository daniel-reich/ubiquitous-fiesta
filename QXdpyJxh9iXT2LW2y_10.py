
def semiprimes(n):
    semi = []
    p = get_primes(n)
    for i in range(len(p)):
        for j in range(i, len(p)):
            if p[i] * p[j] < n:
                semi.append(p[i] * p[j])
            else:
                break
    semi = sorted(semi)
    return (semi, [x for x in semi if x ** 0.5 not in p])
    
def get_primes(n):
    primes = []
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p] == True:
            primes.append(p)
            for i in range(p * p , n, p):
                sieve[i] = False
    return primes

