
def is_factorial(n):
    from math import factorial
    x=[i*factorial(i-1) for i in range(1,7)]
    if n in x:
        return True
    else:
        return False

