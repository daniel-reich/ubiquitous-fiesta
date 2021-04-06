
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True
​
​
def fat_prime(a, b):
    if a < b:
        return max([x for x in range(a, b + 1) if is_prime(x)])
    else:
        return max([x for x in range(b, a) if is_prime(x)])

