
def sieve_of_eratosthenes(max_prime):
    if max_prime <= 1:
        return []
​
    prime_indicators = [True] * (max_prime + 1)
    prime_indicators[0] = False
    prime_indicators[1] = False
    for e in range(2, max_prime // 2 + 1):
        if not prime_indicators[e]:
            continue
        for i in range(e * 2, max_prime + 1, e):
            prime_indicators[i] = False
    primes = [i for i in range(max_prime + 1) if prime_indicators[i]]
    return primes
​
def lcm(nums):
    primes = sieve_of_eratosthenes(max(nums) + 1)
    primes_so_far = []
    for num in nums:
        for p in primes_so_far:
            if num % p == 0:
                num /= p
        for p in primes:
            while num % p == 0:
                primes_so_far.append(p)
                num /= p
    prod = 1
    for p in primes_so_far:
        prod *= p
    return prod

