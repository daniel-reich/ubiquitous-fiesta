
def factorial(n):
# Base case: 1! = 1
    if n == 1 or n == 0:
        return 1
​
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

