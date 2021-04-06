
def is_exact(n, f=1, i=1):
    if f > n:
        return 'Not exact!'
    if f == n:
        return [n, i]
    return is_exact(n, (i+1) * f, i + 1)

