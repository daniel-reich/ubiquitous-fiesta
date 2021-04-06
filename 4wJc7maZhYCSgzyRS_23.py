
def two_product(arr, N):
    lst = []
    for n in arr:
        if not N%n:
            if N//n in lst:
                return [N//n, n]
            lst.append(n)

