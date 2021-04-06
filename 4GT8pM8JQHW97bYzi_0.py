
def primes2(n):
    n, correction = n - n % 6 + 6, 2-(n % 6 > 1)
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
lst_primes2 = primes2(29000)
​
def loneliest_number(lo, hi):
    idx, idx_lo, idx_hi = 0, 0, 0
    if lst_primes2[idx_lo] < lo:
        while lst_primes2[idx_lo] < lo:
            idx_lo += 1
        idx_lo -= 1
    while lst_primes2[idx_hi] < hi:
        idx_hi += 1
    primes = lst_primes2[idx_lo: idx_hi + 1]
    res, max_distance = lo, 0
    for num in range(lo, hi + 1):
        distance = min([abs(num - p) for p in primes if num != p])
        if distance > max_distance:
            res = num
            max_distance = distance
    closest = (res + max_distance if res + max_distance in primes
               else res - max_distance)
    return {'number': res, 'distance': max_distance, 'closest': closest}

