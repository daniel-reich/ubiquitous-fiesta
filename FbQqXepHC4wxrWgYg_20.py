
import math
def isPrime(n):
    if n == 1 or n == 0 :
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True
def prime_divisors(num):
    return [i for i in range(2,num + 1) if num%i == 0 and  isPrime(i) ==True ]

