
import sys 
from math import sqrt
from time import sleep
​
def is_prime(n):
    for i in range(2,int(sqrt(n)) + 1) :
        if n % i == 0 :
            return False 
    else :
        return True 
​
​
​
def prime_factors(num):
    l =[]
    while (num > 1) :
        print(num)
        if is_prime(num):
            l.append(num)
            return l  
        for n in range(2,int(sqrt(num)) + 1) :
            if num % n == 0 and is_prime(n):
                l.append(n)
                print("n: ", n)
                num //= n 
                break 
    return l

