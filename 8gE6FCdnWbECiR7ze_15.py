
from sys import stdout
def isprime(num):
    if num > 1:  
        for i in range(2, num): 
            if (num % i) == 0: 
                return False
                break
            else: 
                return True
    else: 
        return False
def factors(n):
    rt = []
    f = 2
    if n == 1:
        rt.append(1);
    else:
        while 1:
            if 0 == ( n % f ):
                rt.append(f);
                n //= f
                if n == 1:
                    return rt
            else:
                f += 1
    return rt
 
def sum_digits(n):
    sum = 0
    while n > 0:
        m = n % 10
        sum += m
        n -= m
        n //= 10
 
    return sum
 
def add_all_digits(lst):
    sum = 0
    for i in range (len(lst)):
        sum += sum_digits(lst[i])
 
    return sum
​
def smith_type(number):
    if number==1:
        return "Not a Smith"
    if sum_digits(number-2)==add_all_digits(factors(number-2))and sum_digits(number-1)==add_all_digits(factors(number-1)) and sum_digits(number)==add_all_digits(factors(number)):
        return "Oldest Smith"
    if isprime(number):
        return "Trivial Smith"
    if sum_digits(number)==add_all_digits(factors(number))and sum_digits(number-1)==add_all_digits(factors(number-1)):
        return "Youngest Smith"
    if sum_digits(number)==add_all_digits(factors(number)):
        return  "Single Smith"
    if  sum_digits(number)!=add_all_digits(factors(number)):
        return "Not a Smith"

