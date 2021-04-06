
def two_product(arr, n):
    a = set()
    for x in arr:
        target = n // x
        if target in a and target * x == n:
            return [n//x, x]
        else:
            a.add(x)
    return None

