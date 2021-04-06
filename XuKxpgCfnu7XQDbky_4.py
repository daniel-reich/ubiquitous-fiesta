
def sum_and_product(b, c):
    a=1
    d = (b*b - 4*a*c)**0.5
    if complex(d.imag)!=0j:
        return None
    if d==float(d):
        x= round(float(-(-b + d)/(2*a)),3)
        y = round(float(-(-b - d)/(2*a)),3)
        return x,y

