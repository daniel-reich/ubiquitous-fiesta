
def prime(x: int) -> bool:
    return x > 1 and not any(x % i == 0 for i in range(2, x))
​
def semiprimes(n):
    primes = [i for i in range(n + 1) if prime(i) and i < (n / 2)]
    squared = [pow(i, 2) for i in primes if pow(i, 2) < n]
    semiprimes = [i * j for i in primes for j in primes if i * j < n]
​
    l1 = sorted(set(semiprimes))
    l2 = [el for el in l1 if el not in squared]
​
    return (l1, l2)

