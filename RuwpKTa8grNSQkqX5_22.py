
from fractions import Fraction
​
def fractions(decimal):
    d = decimal.replace(')', '').split('(') 
    data = d[0]
    while len(data) < 10:
        data += d[1]
    data = Fraction(float(data)).limit_denominator()
    return str(data.numerator)+"/"+ str(data.denominator)

