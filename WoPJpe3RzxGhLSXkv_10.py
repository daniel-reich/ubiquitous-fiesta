
def concatenation_sum(n):
    ans = 0
    i = 1
    while i <= n:
        ans += (n - i + 1)
        i *= 10
    return ans

