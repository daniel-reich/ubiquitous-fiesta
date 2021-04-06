
def who_goes_free(n, k):
    l = list(range(n))
    k -= 1
    idx = k
    while len(l) > 1:
        l.pop(idx) 
        idx = (idx + k) % len(l)
    return  l[0]

