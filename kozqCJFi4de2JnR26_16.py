
def fib_str(n, str):
    L = str[:]
    a, b = L
    for _ in range(n - 2):
        a, b = b, b + a
        L.append(b)
    return ', '.join(L)

