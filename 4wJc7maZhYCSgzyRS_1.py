
def two_product(arr, n):
    s = set()
    for i in arr:
        if i != 0 and n/i in s and n/i != i:
            return [n/i, i]
        else:
            s.add(i)

