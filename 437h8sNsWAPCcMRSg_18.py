
def product_of_primes(num):
    primes = prime_sieve(num)
    for p in primes:
        if num/p in primes:
            return True
    return False
    
def prime_sieve(num):
    if num < 2:
        return []
    sieve = [True] * num
    sieve[0], sieve[1] = False, False
​
    for i in range(2, int(num ** 0.5) + 1):
        p = i * 2
        while p < num:
            sieve[p] = False
            p += i
    return [i for i in range(num) if sieve[i]]

