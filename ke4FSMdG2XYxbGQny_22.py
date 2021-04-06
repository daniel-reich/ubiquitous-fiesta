
def even_odd_transform(lst, n):
    return [(e-2*n if e%2==0 else e+2*n) for e in lst ]

