
from fractions import Fraction
​
def bintodec(st):
    if '.' not in st:
        return Fraction(int(st,base = 2),1)
    else:
        decimal_point_idx = len(st)-1-st.find('.')
        return Fraction(int(st.replace('.',''),base = 2),2**decimal_point_idx)
​
def binary_sum(lst):
    s = sum(map(bintodec, lst))
    if s.denominator == 1:
        return str(s)
    if s < 1:
        return str(s)
    else:
        return '{} {}'.format(s.numerator//s.denominator, s % 1)

