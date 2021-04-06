
def fibonacci(n):
    a, b, c = 1, 1, 2
    while n > 2:
        a, b = a*a + b*b, a*b + b*c
        c = a + b
        n //= 2
    return b

