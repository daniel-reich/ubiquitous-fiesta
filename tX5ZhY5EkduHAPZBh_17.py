
def nearest_element(n, lst):
    a = list(map(lambda x:[x, abs(x-n)],lst))
    a.sort(key=lambda x:x[1])
    if a[0][1] == a[1][1] :
        return lst.index(a[0][0]) if a[0][0] > a[1][0] else lst.index(a[1][0])
    else:return lst.index(a[0][0])

