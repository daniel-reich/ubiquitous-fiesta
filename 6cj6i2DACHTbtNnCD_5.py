
def two_product(arr, n):
    d = {}
    for i in arr:
        if n%i == 0:
            if i in d:
                return sorted([i, d[i]])
            else:
                d[n//i] = i

