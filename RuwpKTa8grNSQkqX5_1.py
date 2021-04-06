
from fractions import*
from fractions import Fraction
def fractions(decimal):
    x=decimal.replace('(','.').replace(')','')
    a,b,c=x.split('.')
    y=(int(a+b+c)-bool(c)*int(a+b),(10**len(c)-bool(c))*10**len(b))
    #print(Fraction(y[0],y[1]))
    z='%s/%s'%(y[0],y[1])
    return '%s'%(Fraction(y[0])/Fraction(y[1]))

