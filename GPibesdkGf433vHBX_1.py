
def is_prime(n):
    return n == 2 or n % 2 and n > 2 and all(n % i for i in range(3, int(n ** .5) + 1, 2))
​
def goldbach_conjecture(n):
    if n % 2 or n <= 2:
        return []
    return next(([i, n - i] for i in range(2, n // 2 + 1) if is_prime(i) and is_prime(n - i)))

