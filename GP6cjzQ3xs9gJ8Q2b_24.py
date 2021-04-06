
def is_polydivisible(n):
    return all(int(str(n)[:i])/i==int(str(n)[:i])//i for i in range(1, len(str(abs(n)))+1))

