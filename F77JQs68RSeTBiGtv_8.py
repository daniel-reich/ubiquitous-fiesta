
def diamond_sum(n):
    if n == 1:
        return 1
    half = n // 2
    ans = half + 1
    mid = half + 1
    for r in range(1, n - 1):
        mid += n
        ans += 2 * mid
    ans += mid + n
    return ans

