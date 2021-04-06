
def get_prime_factors(n):
​
    i = 2
    prime_factors = []
​
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
​
    if n > 1:
        prime_factors.append(n)
​
    return prime_factors
​
​
def is_powerful(n):
​
    prime_factors = get_prime_factors(n)
​
    unique_prime_factors = tuple(dict.fromkeys(prime_factors))
​
    for p in unique_prime_factors:
        if n % p != 0 or n % (p * p) != 0:
            return False
    return True

