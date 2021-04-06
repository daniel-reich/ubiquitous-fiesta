
def fibonacci(n):
    arr = []
    while n:
        arr.append(n)
        n //= 2
    a, b = 0, 1
    while arr:
        c = a * ((b << 1) - a)
        d = a**2 + b**2
        n = arr.pop()
        if n%2:
            a, b = d, c + d
        else:
            a, b = c, d
    return a

