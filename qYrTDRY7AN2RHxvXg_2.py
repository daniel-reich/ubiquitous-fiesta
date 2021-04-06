
from math import sqrt
def f(A, c):
    D = pow(c,4) - 16 * A * A 
    if D >= 0: 
        root1 = (c * c + sqrt(D))/2
        root2 = (c * c- sqrt(D))/2
        a = round(sqrt(root1),3) 
        b = round(sqrt(root2),3) 
        if b >= a: 
            return [a,b]
        else:
            return [b,a]
    else:
        return  "Does not exist"

