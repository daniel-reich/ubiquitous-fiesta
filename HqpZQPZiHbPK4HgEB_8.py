
def maxmin(n):
    digits = [int(d) for d in str(n)]
    l = len(digits)
    minie = n
    maxie = n
    for i in range(l):
        for j in range(i + 1, l):
            d1, d2 = digits[i], digits[j]
            num = digits[:]
            num[i] = d2
            num[j] = d1
            if num[0] != 0:
                k = int(''.join(map(str, num)))
                minie = min(minie, k)
                maxie = max(maxie, k)
    return (maxie, minie)

