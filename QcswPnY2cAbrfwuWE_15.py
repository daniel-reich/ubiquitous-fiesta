
from math import factorial
​
def isFactorial(n):
    i = 1
    fact = 1
    while(fact < n):
        i += 1
        fact *= i
    return fact == n
​
def filter_factorials(numbers):
    return [i for i in numbers if isFactorial(i)]

