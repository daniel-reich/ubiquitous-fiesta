
from math import sqrt
​
def extract_primes(num):
    digits=[i for i in str(num)]
    primes=[]
​
    set_size=1
​
    while set_size<=len(digits):
        for i in range(len(digits)):
            if i+set_size> len(digits):
                continue
​
            test= "".join(digits[i:i+set_size])
​
            if str(int(test))!= test:
                continue
​
​
            if isPrime(int(test)):
                primes.append(int(test))
        set_size+=1
​
    primes.sort()
    return primes
​
def isPrime(num):
    if num<= 1:
        return False
​
    for n in range (2,int(sqrt(num))+1):
        if num % n==0:
            return False
    return True

