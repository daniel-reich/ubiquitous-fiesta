
def filter_primes(num):
    L = []
    for x in num:
        L += isPrime(x),
    return [x for x in L if type(x) == int]
        
def isPrime(n) : 
    if n == 2 or n == 3:
        return n
    elif n == 1:
        return None
    if (n % 2 == 0 or n % 3 == 0) : 
        return None
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return None
        i = i + 6
    return n

