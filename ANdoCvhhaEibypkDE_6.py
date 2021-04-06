
def closing_in_sum(n):
    ans = 0
    n = str(n)
    for i in range(len(n) // 2):
        ans += int(n[i] + n[-(i+1)])
    if len(n) % 2 == 1:
        ans += int(n[len(n) // 2])
    return ans

