
def diamond_sum(n):
    if n == 1:
        return 1
    m = n // 2
    total = n - m
    lst = [((2 * i + 1) * n) + 1  for i in range(1,n-1)]
    return total + (n * n) - m + sum(lst)

