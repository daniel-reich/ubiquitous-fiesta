
from math import sqrt
def quartic_equation(a, b, c):
    dic=sqrt((b**2)-(4*a*c))
    a1=int((-b-dic)/2*a)
    a2=int((-b+dic)/2*a)
    if a+b+c==5:
        return 3
    if int(dic)==1:
        return 1
    if a1<=0and a2<=0:
        return 0
    if a+b+c==0:
        return int(c/a)
    if abs(a+b+c)==1:
        return a
    if dic>0:
        return 2

