
def is_polydivisible(n):
    n = str(n)
    for i in range(2, len(n)+1):
        if int(n[:i])%i:
            return False
    return True

