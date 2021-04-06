
def simplify(st):
    from fractions import gcd
    st = st.split('/')
    numer = int(st[0]);denom = int(st[1])
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (int(numer / common_divisor), int(denom / common_divisor))
    if reduced_den == 1:
        return str(reduced_num)
    elif common_divisor == 1:
        return str(numer)+'/'+str(denom)
    else:
        return "%d/%d" % (reduced_num, reduced_den)

