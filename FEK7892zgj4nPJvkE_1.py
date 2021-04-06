
def primes2(n):
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3:: 2 * k] = [False] * ((n // 6 - k * k // 6 - 1)
                                                   // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3:: 2 * k] = \
                ([False] * ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) //
                            k + 1))
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction)
                     if sieve[i]]
​
lst_p = primes2(100000)
​
def prime_gaps(g, a, b):
    for x, y in zip(lst_p, lst_p[1:]):
        if x >= a and y <= b and y - x == g:
            return [x, y]

