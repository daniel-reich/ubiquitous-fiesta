
def subsetSum(lst, n, a, b, c):
    if a == b == c == 0:
        return True
    if n < 0:
        return False
    A = False
    if a - lst[n] >= 0:
        A = subsetSum(lst, n - 1, a - lst[n], b, c)
    B = False
    if not A and b - lst[n] >= 0:
        B = subsetSum(lst, n - 1, a, b - lst[n], c)
    C = False
    if not A and not B and c - lst[n] >= 0:
        C = subsetSum(lst, n - 1, a, b, c - lst[n])
    return A or B or C
        
​
def coins_div(lst):
    S = sum(lst)
    if S % 3 != 0:
        return False
    S3 = S // 3
    n = len(lst)
    return subsetSum(lst, n - 1, S3, S3, S3)

