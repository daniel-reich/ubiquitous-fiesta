
def diamond_sum(n):
    return n * n + 1 + (n + 1) * (n - 2) + n * (n - 1) * (n - 2) if n > 1 else 1

