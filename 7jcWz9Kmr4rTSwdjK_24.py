
import math
​
def next_prime(n):
    n += 1
    is_prime = False
    i = 0
    while not is_prime:
        for j in range(2,math.floor(math.sqrt(n))+1):
            if n % j == 0:
                i += 1
        if i == 0:
            is_prime = True
        else:
            n += 1
            i = 0
    return n
​
def prime_factorize(n):
    prime_factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            prime_factors += [i]
            n /= i
        i = next_prime(i)
    return prime_factors

