
import math
def check_prime(n):
    if n <= 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
​
def prime_divisors(num):
    result = []
    for i in range(2, num//2):
        if num % i == 0 and check_prime(i):
            result.append(i)
    if check_prime(num):
        result.append(num)
    return result

