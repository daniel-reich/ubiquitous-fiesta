
from random import randint
​
​
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
​
​
def fastermod(factor, power, modulus):
    res = 1
    while power > 0:
        if power % 2:
            res = res * factor % modulus
            power -= 1
        power //= 2
        factor = (factor * factor) % modulus
    return res
​
​
def is_prime(num):
    for _ in range(20):
        k = randint(1, num - 1)
        if gcd(k, num) > 1:
            return False
        if fastermod(k, num - 1, num) > 1:
            return False
    return True

