
def fib(n):
    a, b = 0, 1; seq = [a, b]
    while len(seq) <= n:
        a, b = b, a+b
        seq.append(b)
    return seq[-1] if n > 1 else seq[n]

