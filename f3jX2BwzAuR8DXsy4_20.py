
def fact_of_fact(n):
    if n == 1:
        return 1
    else:
        return factorial(n) * fact_of_fact(n-1)
​
​
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

