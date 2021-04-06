
def repeated(s):
    n = len(s)
    if n == 1:
        return False
    for k in range(1, n):
        if n % k == 0 and s == s[:k] * (n // k):
            return True
    return False

