
def two_product(lst, n):
    p = []
    for i in lst:
        if (n / i) in lst:
            p.append(i)
            p.append(round(n / i))
            return sorted(p)

