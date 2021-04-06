
from math import factorial as f
def pascals_triangle(r):
    s = ''
    for i in range(r+1):
        s += str(f(r)//(f(i)*f(r-i)))+' '
    return s[:-1]

