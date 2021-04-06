
def sum_and_product(s, p):
    if s*s-4*p<0:return None
    return round((-s+(s*s-4*p)**.5)/-2,3),round((-s-(s*s-4*p)**.5)/-2,3)

