
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
​
def combinations(k, n):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

