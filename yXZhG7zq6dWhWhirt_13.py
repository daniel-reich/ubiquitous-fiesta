
def filter_primes(num):
    
    def is_prime(n):
        p = []
        for i in range(1, n + 1):
            if n % i == 0:
                p.append(i)
        if len(p) == 2:
            return True
        else:
            return False
        
    primes = []
    for i in num:
        if is_prime(i):
            primes.append(i)
    return primes

