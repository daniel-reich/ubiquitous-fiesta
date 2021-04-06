
def complete_factorization(num):
    sieve = [True] * (num + 1)
    
    for x in range(2, int(len(sieve) ** 0.5) + 1):
        if sieve[x]:
            for i in range(x + x, len(sieve), x):
                sieve[i] = False
    lowerPrimes = []
    n = num
    for i in range(2, len(sieve)):
        while n%i==0 and n>=1:
            lowerPrimes.append(i)
            n = n//i
        if n ==1:
            break
    return lowerPrimes

