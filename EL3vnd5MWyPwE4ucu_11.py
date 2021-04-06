
def fibonacci(n):
    a = 0
    b = 1
    for x in range(n-1):
        a, b = b, a+b
    return str(b)

