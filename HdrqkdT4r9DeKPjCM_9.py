
def poly_find(N, k):
    disc = (k*k + 8 * k * (N - 1))**0.5
    if disc % 1: return 0
    r1, r2 = (k + disc)/(2 * k), (k - disc)/(2 * k)
    return int(max(r1, r2))
​
def format_result(pos, k):
    rem = pos%10
    ordsuff = ['th', 'st', 'nd', 'rd'][0 if 10<pos<14 or not rem in [1,2,3] else rem]
    return "{}{} {}-gonal number".format(pos, ordsuff, k)
​
def is_polygonal(n):
    if n < 4: return "0th of all" if n == 1 else False
    res = []
    for k in range(3, n):
        if (n-1)%k == 0:
            pos = poly_find(n, k)
            if pos:
                res.append(format_result(pos-1, k))
    return res

