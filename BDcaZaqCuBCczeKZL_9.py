
def arrow(n):
    if n % 2 == 0:
        return ['>' * k for k in range(1, n + 1)] + ['>' * k for k in range(n, 0, -1)]
    else:
        return ['>' * k for k in range(1, n + 1)] + ['>' * k for k in range(n - 1, 0, -1)]

