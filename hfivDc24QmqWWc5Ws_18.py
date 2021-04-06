
import math
def eratosthenes(num):
    return [i for i in range(2, num+1) if isPrime(i)]
def isPrime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True

