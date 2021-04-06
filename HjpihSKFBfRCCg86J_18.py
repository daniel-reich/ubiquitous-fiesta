
def compound_interest(p, t, r,n):
    for x in range(t):
        for y in range(n):
            p += p*r/n
    return round(p,2)

