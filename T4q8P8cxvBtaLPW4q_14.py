
def isPrime(n):
    import math
    if n <= 1: return False
    numbers_to_check = range(2,math.floor(math.sqrt(n))+1)
    for e in numbers_to_check:
        if n % e == 0:
            return False
    return True
​
def extract_primes(n):
    l = []
    for length in range(1,len(str(n))+1):
        for idx in range(len(str(n))-length+1):
            t = int(str(n)[idx:idx+length])
            if len(str(t)) != length:
                continue
            if isPrime(t):
                l.append(t)
    return sorted(l)

