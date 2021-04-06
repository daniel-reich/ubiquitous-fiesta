
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n % 2:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if not n % k:
            return False
    return True
​
​
def prime_factors(num):
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return res
​
​
def mod_inv(n, m):
    n_factors, m_factors = prime_factors(n), prime_factors(m)
    for i in n_factors:
        if i in m_factors:
            return False
    if is_prime(m):
        base = n
        power = m - 2
        mod = m
        result = 1
        while power > 0:
            if power % 2 == 1:
                result = (result * base) % mod
            power = power // 2
            base = (base * base) % mod
    else:
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = m, n
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        result = old_s
        if result < 0:
            result += m
    return result

