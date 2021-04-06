
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
def digital_root(n):
    while len(str(n)) > 1:
        n = sum(int(c) for c in str(n))
    return n
​
​
def is_smith(n):
    return digital_root(n) == digital_root(sum(prime_factors(n)))
​
​
def smith_type(num):
    if is_prime(num):
        return 'Trivial Smith'
    if not is_smith(num):
        return 'Not a Smith'
    if is_smith(num - 1) and not is_prime(num - 1):
        return 'Oldest Smith'
    elif is_smith(num + 1) and not is_prime(num + 1):
        return 'Youngest Smith'
    else:
        return 'Single Smith'

