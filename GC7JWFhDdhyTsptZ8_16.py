
def sexy_primes(n, limit):
    primes = []
    for num in range(2,limit):
        if all(num % i != 0 for i in range(2,int(num** 0.5)+1)):
            primes.append(num)     
    if n == 2:
        return [(num,num+6) for num in primes if num + 6 in primes]
    return [(num,num+6,num+12) for num in primes if num + 6 in primes and num + 12 in primes]

