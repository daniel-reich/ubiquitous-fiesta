
def almost_palindrome(s):
    l = len(s) // 2
    a, e = s[:l], s[-1:-l - 1:-1]
    count = 0
    for i in range(len(a)):
        if a[i] == e[i]:
            count += 1
    out = False
    if count == l - 1:
        out = True
    return out

