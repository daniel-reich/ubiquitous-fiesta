
def sum_round(num):
    n = len(str(num))
    ans = []
    for p in range(1, n+1):
        p10 = 10**p
        k = num % p10
        if k > 0:
            ans.append(k)
        num -= k
    return ' '.join(map(str, ans))

