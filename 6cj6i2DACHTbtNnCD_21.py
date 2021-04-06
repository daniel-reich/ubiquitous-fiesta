
def two_product(lst, n):
    sList = sorted(lst)
    for i in sList:
        for j in sList:
            if i * j == n:
                return [i, j]
    return

