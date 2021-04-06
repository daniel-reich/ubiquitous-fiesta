
def factorial(n):
    return 1 if n < 2 else factorial(n-1) * n
​
def eval_factorial(lst):
    return sum(factorial(int(s[:-1])) for s in lst)

