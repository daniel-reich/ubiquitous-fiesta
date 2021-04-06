
def combinations(k, n):
    a = 1
    b = 1
    for i in range(1,min(k,n-k)+1):
        a *= n + 1 - i
        b *= i
    return int(a/b)

