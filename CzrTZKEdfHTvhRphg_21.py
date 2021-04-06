
from fractions import Fraction
from fractions import Fraction
def mixed_number(frac):
    nbr = Fraction(frac)
    n, d = nbr.numerator, nbr.denominator
    if n < 0:
        sign = '-'
        n = -n
    else:
        sign = ''
    w, newn = divmod(n, d)
    if w == 0:
        if newn == 0:
            return '0'
        return sign + str(newn) + '/' + str(d)    
    if newn == 0:
        return sign + str(w)
    return sign + str(w) + ' ' + str(newn) + '/' + str(d)

