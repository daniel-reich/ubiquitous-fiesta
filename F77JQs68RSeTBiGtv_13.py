
def diamond_sum(n):
    return 1 if n == 1 else n**2 + 1 + sum(1 + (2 * r  + 1) * n for r in range(1, n - 1))

