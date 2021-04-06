
import math
def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))
​
def pascals_triangle(n):
    return  sum([ [nCr(i,j) for j in range(0,i+1) ] for i in range(0,n) ],[])

