
from fractions import Fraction
​
def farey(n):
    m = 2*n if n % 2 == 0 else 2*n+2
    f = []
    fraclist = []
    
    for den in range(2,n+1):
        for num in range(1,den):
            if not Fraction(str(num) + '/' + str(den)) in fraclist:
                fraclist.append(Fraction(str(num) + '/' + str(den)))
    
    f.append('0/1')
    while len(fraclist) > 0:
        f.append(str(fraclist[fraclist.index(min(fraclist))]))
        fraclist.pop(fraclist.index(min(fraclist)))
    f.append('1/1')
    
    return f

