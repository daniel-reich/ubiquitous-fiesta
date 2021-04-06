
def fib_str(n, txt):
    for _ in range(n - 2):
        txt.append(txt[-1] + txt[-2])
    return ', '.join(txt)

