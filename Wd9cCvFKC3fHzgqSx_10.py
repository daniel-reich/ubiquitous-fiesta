
def num_split(num):
    sign = 1
    if num < 0:
        sign = -1
        num = -num    
    n = len(str(num))
    ans = []
    for p in range(n - 1, -1, -1):
        p10 = 10**p
        ans.append(sign * (num // p10) * p10)
        num %= p10
    return ans

