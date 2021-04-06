
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
​
​
def combinations(k, n):
    return factorial(n) // (factorial(n - k) * factorial(k))

