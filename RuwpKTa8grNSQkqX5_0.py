
from fractions import Fraction 
def fractions(decimal):
    x,y = decimal.split('(')
    y = y.rstrip(')')
    return str(Fraction(str(x) + str(y) * 100).limit_denominator(100000)._numerator) + '/' + str(Fraction(str(x) + str(y) * 100).limit_denominator(100000)._denominator)

