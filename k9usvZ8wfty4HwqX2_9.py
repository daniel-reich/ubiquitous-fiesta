
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
def cuban_prime(num):
    if is_prime(num):
        d2 = 9 + 12 * (num - 1)
        if pow(d2, 0.5).is_integer():
            return "{} is cuban prime".format(num)
    return "{} is not cuban prime".format(num)

