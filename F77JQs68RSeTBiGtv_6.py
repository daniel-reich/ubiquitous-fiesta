
def diamond_sum(n):
    if n == 1:
        return 1
    total = l = r = n//2 + 1
    for _ in range(n//2):
        l += n - 1
        r += n + 1
        total += l + r
    for _ in range(n//2):
        l += n + 1
        r += n - 1
        total += l + r
    return total - r

