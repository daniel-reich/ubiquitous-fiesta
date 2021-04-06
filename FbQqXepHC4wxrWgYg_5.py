
def prime_divisors(num):
    res = set()
    while not num % 2:
        num //= 2
        res.add(2)
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res.add(divisor)
        divisor += 2
    """1 is not a prime factor but author put it into the tests"""
    res.add(1)
    return sorted(res)

