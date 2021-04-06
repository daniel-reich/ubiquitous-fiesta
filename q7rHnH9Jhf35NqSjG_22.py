
def trailing_zeros(N):
    ans = 0
    k = 5
    while k <= N:
        ans += N // k
        k *= 5
    return ans

