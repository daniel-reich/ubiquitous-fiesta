
def quartic_equation(a, b, c):
    s=(4,2,0,3,1)
    r=(b*b-4*a*c)**.5
    x1=(-b+r)/2*a
    x2=(-b-r)/2*a
    return s[(x1<0)+(x2<0)+3*((x1==0) or (x2==0))]

