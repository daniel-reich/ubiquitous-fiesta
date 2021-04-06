
def is_polydivisible(n):
    if n < 9:
        return True
    s = str(n)
    for i in range(2, len(s) + 1):
        if int(s[:i]) % i:
            return False
    return True

